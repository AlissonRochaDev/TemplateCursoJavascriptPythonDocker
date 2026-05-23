# Importando as bibliotecas necessárias.
from flask import request, jsonify, Blueprint

# Criando uma Blueprint (E auxiliar na localização).
calculadora_bp = Blueprint('calculadora', __name__)

# Conteúdo dessa Blueprint.
# SOMAR. ======================================
@calculadora_bp.post("/calcular-soma")
def somar():
    # Pegar os valores no formato JSON.
    dados = request.get_json()

    numero_1 = dados.get("num1")
    numero_2 = dados.get("num2")

    resultado = numero_1 + numero_2

    return jsonify({"SOMA = ": resultado})

# SUBTRAIR. ======================================
@calculadora_bp.post("/calcular-subtracao")
def menos():
    # Pegar os valores no formato JSON.
    dados = request.get_json()

    numero_1 = dados.get("num1")
    numero_2 = dados.get("num2")

    resultado = numero_1 - numero_2

    return jsonify({"SUBTRAÇÃO = ": resultado})

# MULTIPLICAR. ======================================
@calculadora_bp.post("/calcular-vezes")
def vezes():
    # Pegar os valores no formato JSON.
    dados = request.get_json()

    numero_1 = dados.get("num1")
    numero_2 = dados.get("num2")

    resultado = numero_1 * numero_2

    return jsonify({"MULTIPLICAÇÃO = ": resultado})

# DIVIDIR. ======================================
@calculadora_bp.post("/calcular-dividir")
def dividir():
    # Pegar os valores no formato JSON.
    dados = request.get_json()

    numero_1 = dados.get("num1")
    numero_2 = dados.get("num2")

    return jsonify(resultado=numero_1/numero_2)