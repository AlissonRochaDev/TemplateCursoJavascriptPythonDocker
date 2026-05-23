from flask import Blueprint, request, jsonify
import requests

api_bp = Blueprint("api", __name__)

API_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

@api_bp.get("/cotacao-dolar")
def cotacao_dolar():
    try:
        request = requests.get(API_URL)

        if request.status_code != 200:
            return jsonify({"status": f"Erro ao chamar a API. STATUS: {request.status_code}"}) 
        
        dados_cotacao = request.json()

        valor = f"{float(dados_cotacao['USDBRL']['bid']):.2f}"
        moeda = dados_cotacao['USDBRL']['name']

        return jsonify({
            "status": "sucesso",
            "moeda": moeda,
            "valor_real": valor
        })

    except Exception as e:
        return jsonify({"status": "erro", "mensagem": f"Erro geral: {str(e)}"})