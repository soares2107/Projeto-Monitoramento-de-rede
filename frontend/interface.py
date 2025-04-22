import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

API_URL = "http://localhost:5000"

st.set_page_config(page_title="Monitoramento de Rede", layout="wide")
st.title("📡 Monitoramento de Dispositivos de Rede")

# Inicializa os valores dos campos
for key, default in {"ip": "", "nome": "", "trafego": 0.0}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# Formulário de registro
st.header("Registrar novo dispositivo")
with st.form("form_dispositivo"):
    st.text_input("Endereço IP", key="ip")
    st.text_input("Nome do dispositivo", key="nome")
    st.number_input("Taxa de tráfego (Mbps)", min_value=0.0, step=1.0, key="trafego")
    submitted = st.form_submit_button("Adicionar")

    if submitted:
        dados = {
            "ip": st.session_state["ip"],
            "nome": st.session_state["nome"],
            "trafego": st.session_state["trafego"]
        }

        if dados["ip"] and dados["nome"]:
            resp = requests.post(f"{API_URL}/dispositivos", json=dados)
            if resp.status_code == 200:
                st.success("Dispositivo registrado com sucesso!")
                components.html("<script>window.top.location.reload();</script>", height=0)
            else:
                st.error("Erro ao registrar dispositivo.")
        else:
            st.warning("Preencha todos os campos.")

# Container que engloba todo o conteúdo dinâmico
conteudo = st.empty()

with conteudo.container():
    st.header("📊 Dashboard de Dispositivos")

    try:
        resposta = requests.get(f"{API_URL}/dispositivos")
        if resposta.status_code == 200:
            dispositivos = resposta.json()

            if dispositivos:
                for d in dispositivos:
                    d["status"] = "Normal" if d["trafego"] <= 50 else "Alto"

                df = pd.DataFrame(dispositivos)

                st.subheader("📋 Tabela de dispositivos")
                st.dataframe(df[["id", "nome", "ip", "trafego", "status"]].rename(columns={
                    "id": "ID", "nome": "Nome", "ip": "IP",
                    "trafego": "Tráfego (Mbps)", "status": "Status"
                }), use_container_width=True)

                st.subheader("📈 Gráfico de Tráfego por Dispositivo")
                fig = px.bar(
                    df,
                    x="nome",
                    y="trafego",
                    color="status",
                    color_discrete_map={"Normal": "blue", "Alto": "red"},
                    labels={"nome": "Dispositivo", "trafego": "Mbps"},
                    title="Tráfego de Rede por Dispositivo"
                )
                st.plotly_chart(fig, use_container_width=True)

                st.subheader("🗑️ Remover Dispositivo")
                for d in dispositivos:
                    if st.button(f"Remover {d['nome']} (ID {d['id']})", key=f"del_{d['id']}"):
                        try:
                            response = requests.delete(f"{API_URL}/dispositivos/{d['id']}")
                            if response.status_code == 200:
                                st.success(f"Dispositivo '{d['nome']}' removido com sucesso!")
                                components.html("<script>window.top.location.reload();</script>", height=0)
                            else:
                                st.error("Erro ao remover o dispositivo.")
                        except:
                            st.error("Erro de conexão ao remover dispositivo.")
            else:
                st.info("Nenhum dispositivo registrado.")
        else:
            st.error("Erro ao buscar dispositivos.")
    except:
        st.error("Erro de conexão com o backend.")
