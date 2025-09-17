class Servico:
        
    def __init__(self, descricao: str, valor: float, horario_duracao: float):
        self.__descricao = descricao
        self.__valor = valor
        self.__horario_duracao = horario_duracao

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def nome(self, valor):
        self.__valor = valor
    
    @property
    def horario_duracao(self):
        return self.__horario_duracao
    
    @horario_duracao.setter
    def nome(self, horario_duracao):
        self.__horario_duracao = horario_duracao