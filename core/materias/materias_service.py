from core.materias.materias_repository import MateriasRepository

class AlunoService:
    def __init__(self):
        self.repository = MateriasRepository

    def listar_alunos(self):
        return self.repository.listar()