# 📡 Monitoramento de Dispositivos de Rede

Aplicação web para simulação de monitoramento de tráfego de rede em uma infraestrutura local. Desenvolvida com **Flask** (backend), **Streamlit** (frontend), **SQLite** (banco de dados) e empacotada com **Docker**.

---

## 🧩 Funcionalidades

- Registro de dispositivos com IP, nome e taxa de tráfego simulada (em Mbps)
- Visualização em tempo real da lista de dispositivos e status do tráfego:
  - 🔵 Normal (≤ 50 Mbps)
  - 🔴 Alto (> 50 Mbps)
- Remoção de dispositivos com feedback visual
- Integração entre frontend e backend via API REST
- Execução completa via Docker Compose

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.13-slim](https://hub.docker.com/_/python)
- [Flask](https://flask.palletsprojects.com/)
- [Streamlit](https://streamlit.io/)
- [SQLite](https://www.sqlite.org/index.html)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 📁 Estrutura de Pastas

```
Atividade 4-WEB FULL-STACK/
├── backend/              # API Flask + banco SQLite
│   ├── app.py
│   ├── database.py
│   └── requirements.txt
├── frontend/             # Interface Streamlit
│   ├── interface.py
│   └── requirements.txt
├── docker/               # Dockerfile e Compose
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs/                 # Documentação do projeto
│   └── README.md
└── .gitignore
```

---

## 🚀 Como Executar o Projeto

### ✅ Pré-requisitos

- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados

---

### 🔧 Passos para rodar com Docker

1. Vá para a pasta `docker`:

```bash
cd docker
```

2. Construa e execute os containers:

```bash
docker-compose up --build
```

3. Acesse no navegador:

- Frontend (Streamlit): [http://localhost:8501](http://localhost:8501)
- Backend (API Flask): [http://localhost:5000/dispositivos](http://localhost:5000/dispositivos)

---

## 📄 Licença

Este projeto é apenas para fins educacionais (atividade da disciplina de Redes de Computadores).

---

## ✒️ Autor

- **Joao Gabriel Soares**
- Curso: Ciência da Computação
- Universidade: [Pontifícia Universidade Católica de Goiás]
