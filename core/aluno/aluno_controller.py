# controller do aluno
from flask import Blueprint, request, jsonify
from core.aluno.aluno_service import AlunoService
from core.aluno.aluno import Aluno
from core.autenticacao.autenticacao import autenticacao # estou criando a autenticação em alguns endpints

aluno_service = AlunoService()

aluno_controller = Blueprint('aluno', __name__, url_prefix='/alunos')

@aluno_controller.route('/', methods=['GET'])
@autenticacao # antes de exibir os alunos ele passa pela validação da autenticação
def listar_alunos():
   alunos = aluno_service.listar_alunos()
   return jsonify(alunos)

@aluno_controller.route('/', methods=['POST'])
@autenticacao # antes de exibir os alunos ele passa pela validação da autenticação
def adicionar_aluno():
   dados = request.get_json()
   obj_aluno = Aluno(id=0, nome=dados["nome"], idade=dados["idade"], cpf=dados["cpf"])
   aluno_service.adicionar_aluno(obj_aluno)
   aluno = aluno_service.adicionar_aluno(obj_aluno)
   return jsonify(aluno), 201

@aluno_controller.route('/<int:id>', methods=['GET']) # /<int:id> coloco isto para passar o id pela url
@autenticacao # antes de exibir os alunos ele passa pela validação da autenticação
def obter_aluno(id):
    aluno = aluno_service.obter_aluno_por_id(id)  # ✅ usa a instância
    if aluno:
        return jsonify(aluno), 200
    else:
        return jsonify({"erro": "Aluno não encontrado"}), 404

   
@aluno_controller.route('/<int:id>', methods=['DELETE']) # /<int:id> coloco isto para passar o id pela url
@autenticacao # antes de exibir os alunos ele passa pela validação da autenticação
def remover_aluno(id):
   sucesso = aluno_service.remover_aluno(id)
   return jsonify(sucesso), 200

@aluno_controller.route('/', methods=['PUT'])
@autenticacao # antes de exibir os alunos ele passa pela validação da autenticação
def atualizar_aluno():
   dados = request.get_json()
   obj_aluno = Aluno(id=dados["id"], nome=dados["nome"], idade=dados["idade"], cpf=dados["cpf"])
   aluno = aluno_service.atualizar_aluno(obj_aluno)
   if aluno:
      return jsonify(aluno), 200
   else:
      return jsonify({"erro": "Aluno não encontrado"}), 404