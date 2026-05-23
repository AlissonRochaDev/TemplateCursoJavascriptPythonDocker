from flask import request, jsonify, Blueprint

laco_repeticao_bp = Blueprint("laco_repeticao", __name__)

# f"{total:.2f}"} - Tratamento para Casas Decimais.

# Laço de Repetição FOR!
@laco_repeticao_bp.post("/somar_for")
def somar_com_for():
    try:
        dados = request.get_json()
        precos = dados.get("precos")

        total = 0

        for valor in precos:
            # total = total + valor
            total += valor

        return jsonify({"Total dos Valores com FOR: ": f"{total:.2f}"})

    except Exception as e:
        return jsonify({"Resultado: ": f"Ocorreu um ERRO: {str(e)}"}), 500
    
# Laço de Repetição WHILE!
@laco_repeticao_bp.post("/somar_while")
def somar_com_while():
    try:
        dados = request.get_json()
        precos = dados.get("precos")

        i = 0
        total = 0

        while i < len(precos):
            total += precos[i]
            i += 1

        return jsonify({"Total dos Valores com WHILE: ": f"{total:.2f}"})

    except Exception as e:
        return jsonify({"Resultado: ": f"Ocorreu um ERRO: {str(e)}"}), 500