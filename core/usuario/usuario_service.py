from core.usuario.usuario_repository import UsuarioRepository

class AlunoService:
    def __init__(self):
        self.repository = UsuarioRepository

    def listar_alunos(self):
        return self.repository.listar()