# esse é o modelo Usuário

class Usuario:
    def __init__(self, id=0, nome="", senha=0, status=0):
        self.__id = id
        self.__nome = nome
        self.__senha = senha
        self.__status = status
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha
  
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, novo_status):
        self.__status = novo_status


