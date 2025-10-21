import base64 # usado para criptografar a URL que envia do front para o backend
from functools import wraps # wraps é um decorator para função que vamos passar através dele
from flask import request, jsonify

from core.usuario.usuario_service import UsuarioService

def autenticacao(f):
    @wraps(f) # @wraps serve para preservar o nome da função, posso criar vários e chamar uma única vez
    def decorated(*args, **kwargs): # kwargs quer dizer que eu posso passar dicionários, e preciso sempre criar desta forma
        auth = request.headers.get("Authorization") # vamos configurar isso no Postman

        if not auth or not auth.startswith("Basic "):
            return jsonify({"erro": "Credenciais ausentes"}), 401

        # Remove o prefixo "Basic "
        token = auth.split(" ")[1]
        try:
            # Decodifica Base64 usuario:senha
            decoded = base64.b64decode(token).decode("utf-8")
            usuario, senha = decoded.split(":")
        except Exception:
            return jsonify({"erro": "Credenciais inválidas"}), 401

        # Verifica o usuário cadastrado no banco de dados e suas credenciais de acesso
        service = UsuarioService()
        user = service.obter_usuario_por_usuario_senha(usuario, senha)
        if (not user or user["senha"] != senha or not user["ativo"] or user["usuario"] != usuario):
            return jsonify({"erro": "Usuário ou senha inválidos"}), 401

        return f(*args, **kwargs)

    return decorated # retorna a função que esta dentro da função