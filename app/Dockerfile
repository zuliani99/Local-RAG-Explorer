# Usa una versione leggera di Python
FROM python:3.10-slim

# Imposta la cartella di lavoro dentro il container
WORKDIR /app

# Copia il file dei requisiti e installa le librerie
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il contenuto della tua cartella dentro il container
COPY . .

# Esponi la porta usata da Streamlit
EXPOSE 8501

# Comando per avviare l'app
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]