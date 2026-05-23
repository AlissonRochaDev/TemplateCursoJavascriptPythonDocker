# Arquivo index para iniciar o projeto no Container do Docker.
from flask import Flask, jsonify, request, send_from_directory

# Imoprtando a Blueprint criada (Junto com o caminho do arquivo).
from exemplos.calculos.calculadora import calculadora_bp
from exemplos.condicionais.condicionais_calculadora import condicionais_calculos_bp
from exemplos.condicionais.media import media_bp
from exemplos.laco_repeticao.laco_repeticao import laco_repeticao_bp
from exemplos.colecoes.carrinho_compra import carrinho_compra_bp
from exemplos.arquivos.manipulacao_arquivos import arquivos_bp
from exemplos.api.cotacao_dolar import api_bp

# Declarando uma Variável em Python.
app = Flask(__name__)

# Registra a chamada dos END-POINTS da Blueprint.
app.register_blueprint(calculadora_bp)
app.register_blueprint(condicionais_calculos_bp)
app.register_blueprint(media_bp)
app.register_blueprint(laco_repeticao_bp)
app.register_blueprint(carrinho_compra_bp)
app.register_blueprint(arquivos_bp)
app.register_blueprint(api_bp)

@app.get("/")
def home():
    return "Projeto Flask funcionando!"

# Selo de Rota para chamar no Navegador (URL).
@app.get("/chamar-tela")

@app.get("/calculos/calculadora")
def calculadora():
    return send_from_directory("front_end/calculos", "calcular.html")

# def - função para retorno de uma mensagem.
def inicial():
    return "Seja bem-vindo ao Módulo Python!"