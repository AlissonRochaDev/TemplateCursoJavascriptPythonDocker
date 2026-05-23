from flask import request, jsonify, Blueprint
media_bp = Blueprint("media", __name__)

@media_bp.post("/calcular_media")
def calcular_media():
    try:

        # .strip() - Remove o excesso de espaço dos dois lados do dado!
        dados = request.get_json()
        nome = dados.get("nome").strip()
        nota1 = float(dados.get("nt1"))
        nota2 = float(dados.get("nt2"))
        nota3 = float(dados.get("nt3"))
        nota4 = float(dados.get("nt4"))

        if nome == "":
            return jsonify({"Resultado": "Preencher o campo obrigatório NOME!"}), 400

        if nota1 < 0 or nota1 > 100:
            return jsonify({"Resultado": "A NOTA 1 deverá ser entre 0 e 100."}), 400
        
        if nota2 < 0 or nota2 > 100:
            return jsonify({"Resultado": "A NOTA 2 deverá ser entre 0 e 100."}), 400
        
        if nota3 < 0 or nota3 > 100:
            return jsonify({"Resultado": "A NOTA 3 deverá ser entre 0 e 100."}), 400
        
        if nota4 < 0 or nota4 > 100:
            return jsonify({"Resultado": "A NOTA 4 deverá ser entre 0 e 100."}), 400
        
        # Chamando uma function em Python
        media = obter_media(nota1, nota2, nota3, nota4)
        classificacao = obter_classificacao(media)

        return jsonify({
            "Nome: ": nome,
            "Média: ": media,
            "Classificação: ": classificacao
        })

    except ValueError:
        return jsonify({"Resultado": "As NOTAS deverão ser numéricas!"}), 400

    except Exception as e:
        return jsonify({"Resultado": f"Ocorreu um ERRO: {str(e)}"}), 500
    
# Function em Python
def obter_media(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    return media

def obter_classificacao(media):
    # Verifica se a média esta entre 0 e 40!
    if 0 <= media < 40:
        classificacao = "REPROVADO"
    elif 40 <= media < 60:
        classificacao = "EXAME"
    else:
        classificacao = "APROVADO"
    return classificacao