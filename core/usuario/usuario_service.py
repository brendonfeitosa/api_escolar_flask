from core.usuario.usuario_repository import UsuarioRepository
from core.usuario.usuario import Usuario  # vou usar o modelo aluno para validações

class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()

    def listar_alunos(self):
        return self.repository.listar()
    
    def adicionar_aluno(self, usuario):
        if isinstance(usuario, Usuario):
            return self.repository.adicionar(usuario)
        else:
            return None
    
    def atualizar_usuario(self, usuario):
        if isinstance(usuario, Usuario):
            if usuario.id > 0:
                return self.repository.atualizar(usuario)
            else:
                return "ID do usuario é obrigatório para a atualização!"
        else:
            return None
        
    def remover_usuario(self, usuario_id):
        sucesso = self.repository.remover(usuario_id)
        if not sucesso:
            return None
        else:
            return {"id": usuario_id, "removido": True}
    
    def obter_usuario_por_id(self, usuario_id):
        usuario = self.repository.obter_por_id(usuario_id)
        if not usuario:
            return None
        else:
            return usuario