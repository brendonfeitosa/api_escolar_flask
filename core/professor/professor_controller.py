# controller do aluno
from flask import Blueprint, request, jsonify
from core.professor.professor_service import ProfessorService
from core.professor.professor import Professor
from core.autenticacao.autenticacao import autenticacao # estou criando a autenticação em alguns endpints

professor_service = ProfessorService()

professor_controller = Blueprint('professor', __name__, url_prefix='/professores')

@professor_controller.route('/', methods=['GET'])
@autenticacao # antes de exibir os professors ele passa pela validação da autenticação
def listar_professores():
   professores = professor_service.listar_professores()
   return jsonify(professores)

@professor_controller.route('/', methods=['POST'])
@autenticacao # antes de exibir os professors ele passa pela validação da autenticação
def adicionar_professor():
   dados = request.get_json()
   obj_professor = Professor(id=0, nome=dados["nome"], idade=dados["idade"], formacao=dados["formacao"])
   professor = professor_service.adicionar_professor(obj_professor)
   return jsonify(professor), 201

@professor_controller.route('/<int:id>', methods=['GET']) # /<int:id> coloco isto para passar o id pela url
@autenticacao # antes de exibir os professors ele passa pela validação da autenticação
def obter_professor(id):
    professor = professor_service.obter_professor_por_id(id)  # ✅ usa a instância
    if professor:
        return jsonify(professor), 200
    else:
        return jsonify({"erro": "professor não encontrado"}), 404

   
@professor_controller.route('/<int:id>', methods=['DELETE']) # /<int:id> coloco isto para passar o id pela url
@autenticacao # antes de exibir os professors ele passa pela validação da autenticação
def remover_professor(id):
   sucesso = professor_service.remover_professor(id)
   return jsonify(sucesso), 200

@professor_controller.route('/', methods=['PUT'])
@autenticacao # antes de exibir os professors ele passa pela validação da autenticação
def atualizar_professor():
   dados = request.get_json()
   obj_professor = Professor(id=dados["id"], nome=dados["nome"], idade=dados["idade"], formacao=dados["formacao"])
   professor = professor_service.atualizar_professor(obj_professor)
   if professor:
      return jsonify(professor), 200
   else:
      return jsonify({"erro": "professor não encontrado"}), 404