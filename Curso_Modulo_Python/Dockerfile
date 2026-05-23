# Comunica com o Docker onde esta a imagem do projeto em Python!
FROM python:3.12-slim

# Instrução onde esta as pastas dentro do Container do Docker, onde estara o Projeto em Python!
WORKDIR /app

# requests - É adicionado apenas na ultima aula, para que o Docker possa consumir uma API externa no Projeto Python.
# Chama todas as bibliotecas necessárias para rodar o Projeto em Python dentro do Docker!
# RUN pip install --no-cache-dir "Flask>=3,<4"
RUN pip install --no-cache-dir "Flask>=3,<4" requests

# Copia os arquivos da Pasta Local para dentro das Pastas do Container no Docker!
COPY . .

# Porta para comunicar e rodar o Projeto com o Docker!
EXPOSE 5000