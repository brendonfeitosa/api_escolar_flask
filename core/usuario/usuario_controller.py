# controller do usuario
from flask import Blueprint, request, jsonify
from core.usuario.usuario_service import UsuarioService
from core.usuario.usuario import Usuario
from core.autenticacao.autenticacao import autenticacao

usuario_service = UsuarioService()

usuario_controller = Blueprint('usuario', __name__, url_prefix='/usuarios')

@usuario_controller.route('/', methods=['GET'])
@autenticacao # antes de exibir os alunos ele passa pela validação da autenticação
def listar_usuarios():
   usuarios = usuario_service.listar_usuarios()
   return jsonify(usuarios)

@usuario_controller.route('/', methods=['POST'])
@autenticacao # antes de exibir os alunos ele passa pela validação da autenticação
def adicionar_usuario():
   dados = request.get_json()
   obj_usuario = Usuario(id=0, usuario=dados["usuario"], senha=dados["senha"], ativo=dados["ativo"])
   usuario = usuario_service.adicionar_usuario(obj_usuario)
   return jsonify(usuario), 201

@usuario_controller.route('/<int:id>', methods=['GET']) # /<int:id> coloco isto para passar o id pela url
@autenticacao # antes de exibir os alunos ele passa pela validação da autenticação
def obter_usuario(id):
    usuario = usuario_service.obter_usuario_por_id(id)  # ✅ usa a instância
    if usuario:
        return jsonify(usuario), 200
    else:
        return jsonify({"erro": "Usuario não encontrado"}), 404

   
@usuario_controller.route('/<int:id>', methods=['DELETE']) # /<int:id> coloco isto para passar o id pela url
@autenticacao # antes de exibir os alunos ele passa pela validação da autenticação
def remover_usuario(id):
   sucesso = usuario_service.remover_usuario(id)
   return jsonify(sucesso), 200

@usuario_controller.route('/', methods=['PUT'])
@autenticacao # antes de exibir os alunos ele passa pela validação da autenticação
def atualizar_usuario():
   dados = request.get_json()
   obj_usuario = Usuario(id=dados["id"], usuario=dados["usuario"], senha=dados["senha"], ativo=dados["ativo"])
   usuario = usuario_service.atualizar_usuario(obj_usuario)
   if usuario:
      return jsonify(usuario), 200
   else:
      return jsonify({"erro": "Usuário não encontrado"}), 404

@usuario_controller.route('/<string:usuario>/<string:senha>', methods=['GET']) # /<int:usuario>/<str:senha> coloco isto para passar o id pela url
@autenticacao # antes de exibir os alunos ele passa pela validação da autenticação
def obter_usuario_por_usuario_senha(usuario, senha):
    usuario = usuario_service.obter_usuario_por_usuario_senha(usuario, senha)  # ✅ usa a instância
    if usuario:
        return jsonify(usuario), 200
    else:
        return jsonify({"erro": "usuario não encontrado"}), 404
   
"""  
Essas funções não serão usadas, vamos chamar ela no arquivo de autenticação


#fazer a busca do usuário sem passar pela URL
@usuario_controller.route('/login', methods=['POST'])
def obter_usuario_por_user_senha():
    dados = request.get_json()
    obj_usuario = Usuario(usuario=dados['usuario'], senha=dados['senha'])
    usuario = usuario_service.obter_usuario_por_user_senha(obj_usuario)
    if usuario:
        return jsonify(usuario), 200
    else:
        return jsonify({"erro": "Usuário não encontrado"}), 404
"""