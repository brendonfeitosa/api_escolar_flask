# controller do aluno
from flask import Blueprint, request, jsonify
from core.materias.materias_service import MateriaService
from core.materias.materias import Materia
from core.autenticacao.autenticacao import autenticacao # estou criando a autenticação em alguns endpints

materia_service = MateriaService()

materia_controller = Blueprint('materia', __name__, url_prefix='/materias')

@materia_controller.route('/', methods=['GET'])
@autenticacao # antes de exibir os materias ele passa pela validação da autenticação
def listar_materias():
   materias = materia_service.listar_materias()
   return jsonify(materias)

@materia_controller.route('/', methods=['POST'])
@autenticacao # antes de exibir os materias ele passa pela validação da autenticação
def adicionar_materia():
   dados = request.get_json()
   obj_materia = Materia(id=0, nome=dados["nome"], sigla_curricular=dados["sigla_curricular"], descricao=dados["descricao"])
   materia = materia_service.adicionar_materia(obj_materia)
   return jsonify(materia), 201

@materia_controller.route('/<int:id>', methods=['GET']) # /<int:id> coloco isto para passar o id pela url
@autenticacao # antes de exibir os materias ele passa pela validação da autenticação
def obter_materia(id):
    materia = materia_service.obter_materia_por_id(id)  # ✅ usa a instância
    if materia:
        return jsonify(materia), 200
    else:
        return jsonify({"erro": "materia não encontrado"}), 404

   
@materia_controller.route('/<int:id>', methods=['DELETE']) # /<int:id> coloco isto para passar o id pela url
@autenticacao # antes de exibir os materias ele passa pela validação da autenticação
def remover_materia(id):
   sucesso = materia_service.remover_materia(id)
   return jsonify(sucesso), 200

@materia_controller.route('/', methods=['PUT'])
@autenticacao # antes de exibir os materias ele passa pela validação da autenticação
def atualizar_materia():
   dados = request.get_json()
   obj_materia = Materia(id=dados["id"], nome=dados["nome"], sigla_curricular=dados["sigla_curricular"], descricao=dados["descricao"])
   materia = materia_service.atualizar_materia(obj_materia)
   if materia:
      return jsonify(materia), 200
   else:
      return jsonify({"erro": "materia não encontrado"}), 404