# Utiliza uma imagem oficial do Python
FROM python:3.11-slim
 
# Instala o SQLite e outras dependências necessárias
RUN apt-get update && \
    apt-get install -y sqlite3 libsqlite3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
 
# Define o diretório de trabalho
WORKDIR /app
 
# Copia os arquivos do projeto para o container
COPY . /app
 
# Instala as dependências do Python
RUN pip install --no-cache-dir Flask bcrypt PyJWT
 
# Expõe a porta onde o Flask rodará
EXPOSE 5000
 
# Define a variável de ambiente para o Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
 
# Comando para iniciar a aplicação
CMD ["flask", "run"]