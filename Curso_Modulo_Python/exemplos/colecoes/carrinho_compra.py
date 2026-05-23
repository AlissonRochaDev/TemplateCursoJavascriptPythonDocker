from flask import request, jsonify, Blueprint

carrinho_compra_bp = Blueprint("carrinho_compras", __name__)

precos_produto = {
    "SSD": 220.50,
    "Memória RAM": 320.70
}

@carrinho_compra_bp.post("/processar_pedido")
def processar_pedido_compra():
    try:
        # Pegar as Informações.
        dados_pedido = request.get_json()

        # Pegando o NOME do Cliente
        nome_cliente = dados_pedido.get("cliente").strip()
        carrinho = dados_pedido.get("carrinho")

        if nome_cliente == "":
            return jsonify({"Resultado: ": "É necessário informar o NOME DO CLIENTE!"}), 400
        
        if not isinstance(carrinho, list):
            return jsonify({"Resultado: ": "O CARRINHO está no formato INCORRETO!"}), 400
        
        if not carrinho:
            return jsonify({"Resultado: ": "Carrinho esta VAZIO!"}), 400
        
        valor_total = 0

        for item in carrinho:
            if not isinstance(item, dict):
                return jsonify({"Resultado: ": "Item INVÁLIDO!"}), 400
            
            produto = item.get("produto").strip()
            quantidade = item.get("quantidade")

            if produto == "" or not isinstance(produto, str):
                return jsonify({"Resultado: ": "Produto INVÁLIDO!"}), 400
            
            if not isinstance(quantidade, int) or quantidade <= 0:
                return jsonify({"Resultado: ": "Quantidade INVÁLIDA!"}), 400
            
            if produto not in precos_produto:
                return jsonify({"Resultado: ": "Produto NÃO ENCONTRADO!"}), 400
            
            preco_unitario = precos_produto[produto]
            valor_tem = preco_unitario * quantidade
            valor_total += valor_tem

            # Resposta Final: TUPLA!
            status = ("Processado com SUCESSO!", 200)

            # Resposta em DICIONÁRIO!
            resposta = {
                "cliente": nome_cliente,
                "valor_total": valor_total,
                "status": status[0],
                "status_codigo": status[1]
            }

            return jsonify(resposta)

    except Exception as e:
        return jsonify({"Resultado: ": f"Ocorreu um ERRO: {str(e)}"}), 500