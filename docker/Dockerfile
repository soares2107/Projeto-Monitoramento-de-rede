FROM python:3.13-slim

WORKDIR /app

# Copia os códigos
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# Instala as dependências Python
RUN pip install --no-cache-dir -r backend/requirements.txt && \
    pip install --no-cache-dir -r frontend/requirements.txt

EXPOSE 5000
EXPOSE 8501

CMD ["sh", "-c", "python backend/app.py & streamlit run frontend/interface.py --server.port=8501 --server.address=0.0.0.0"]
