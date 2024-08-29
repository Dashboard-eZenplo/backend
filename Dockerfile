FROM python:3.10-alpine

# Instale dependências do sistema
RUN apk add --no-cache \
    build-base \
    linux-headers \
    gcc \
    libffi-dev \
    musl-dev \
    jpeg-dev \
    zlib-dev \
    mariadb-dev

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copie todo o código do projeto para o diretório de trabalho
COPY ./app /app

# Exponha a porta usada pelo FastAPI
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
