from core.professor.professor_repository import ProfessorRepository

class AlunoService:
    def __init__(self):
        self.repository = ProfessorRepository
    def listar_alunos(self):
        return self.repository.listar()