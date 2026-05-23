from flask import Blueprint, request, jsonify
import os

arquivos_bp = Blueprint("arquivos", __name__)

DIRETORIO_ARQUIVOS = "arquivos/arq_gerados"

# Verificação, se existe um arquivo com nome repetido.
def verificar_arquivo(caminho_completo):
    if not os.path.exists(caminho_completo):
        return False
    return True

# Criando os arquivos =============================================================================================.
@arquivos_bp.post("/criar-arquivos")
def criar():
    try:
        dados = request.get_json()

        nome_arquivo = dados.get("nome").strip()
        conteudo = dados.get("conteudo").strip()

        if(nome_arquivo == "" or conteudo == ""):
            return jsonify({"status:": "erro", "mensagem:": f"Informar o NOME e o CONTEÚDO do arqivo: {str(e)}"}), 400
        
        # Caso a Pasta não exista, ele cria!
        if not os.path.exists(DIRETORIO_ARQUIVOS):
            os.makedirs(DIRETORIO_ARQUIVOS)

        caminho_completo = os.path.join(DIRETORIO_ARQUIVOS, nome_arquivo)

        if verificar_arquivo(caminho_completo):
            return jsonify({"status:": "erro", "mensagem:": f"O ARQUIVO '{nome_arquivo}', já existe!"}), 400

        with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)

        return jsonify({"status:": "sucesso", "mensagem:": f"Arquivo '{nome_arquivo}' foi criado com SUCESSO!"}), 200

    except Exception as e:
        return jsonify({"status:": "erro", "mensagem:": f"ERRO ao cirar o ARQUIVO: {str(e)}"}), 500
    
# Listagem dos aqruivos =============================================================================================.
@arquivos_bp.get("/listar-arquivos")
def listar():
    arquivos = os.listdir(DIRETORIO_ARQUIVOS)
    lista_arquivos = []

    for item_arquivo in arquivos:
        caminho_completo = os.path.join(DIRETORIO_ARQUIVOS, item_arquivo)

        conteudo = ""

        with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

        lista_arquivos.append({
            "nome": item_arquivo,
            "conteudo": conteudo
        })

        return jsonify({"status:": "sucesso", "arquivos:": lista_arquivos}), 200

# Alteração de arquivo já gerado =============================================================================================.
@arquivos_bp.put("/alterar-arquivo")
def alterar():
    try:
        dados = request.get_json()
        nome_arquivo = dados.get("nome").strip()
        novo_conteudo = dados.get("conteudo").strip()

        if nome_arquivo == "" or novo_conteudo == "":
            return jsonify({"status:": "erro", "mensagem:": "Informar o NOME e o CONTEÚDO do arquivo!"}), 400
        
        caminho_completo = os.path.join(DIRETORIO_ARQUIVOS, nome_arquivo)

        if not verificar_arquivo(caminho_completo):
            return jsonify({"status:": "erro", "mensagem:": f"O Arquivo '{nome_arquivo}' não foi ENCONTRADO!"}), 400
        
        with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(novo_conteudo)

        return jsonify({"status:": "sucesso", "mensagem:": f"Conteúdo do '{nome_arquivo}' alterado com SUCESSO!"}), 200

    except Exception as e:
        return jsonify({"status:": "erro", "mensagem:": f"ERRO ao alterar o ARQUIVO: {str(e)}"}), 500

# Exclusão de arquivo já gerado =============================================================================================.
@arquivos_bp.delete("/excluir-arquivo")
def excluir():
    try:
        dados = request.get_json()
        nome_arquivo = dados.get("nome").strip()

        if nome_arquivo == "":
            return jsonify({"status:": "erro", "mensagem:": "Informar o NOME do arquivo para exclusão!"}), 400
        
        caminho_completo = os.path.join(DIRETORIO_ARQUIVOS, nome_arquivo)

        if not verificar_arquivo(caminho_completo):
            return jsonify({"status:": "erro", "mensagem:": "Não foi encontrado o arquivo para ser EXCLUÍDO!"}), 400
        
        # Remove fisicamente o arquivo.
        os.remove(caminho_completo)

        return jsonify({"status:": "sucesso", "mensagem:": f"Arquivo '{nome_arquivo}', excluido com SUCESSO!"}), 200

    except Exception as e:
        return jsonify({"status:": "erro", "mensagem:": f"ERRO ao excluir o ARQUIVO: {str(e)}"}), 500