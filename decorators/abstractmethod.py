"""
    abstractmethod para qualquer método já decorado (@property e setter)
    É possível criar @property @property.setter @classmethod
    @staticmethod e métodos normais como abstratos, para isso
    use @abstractmethod como decorator mais interno.
    Foo - Bar são palavras usadas como placeholder
    para palavras que podem mudar na programação.
"""
from abc import ABC, abstractmethod

#Duas opções de execução, basta inventer o que esta comentado com o que nao esta
class AbstarctFoo(ABC):
    def __init__(self, nome) -> None:
        self.nome = nome
    
    @property
    # @abstractmethod
    def nome(self):
        # ...
        return self._nome
    
    # @nome.setter
    # @abstractmethod
    # def nome(self, nome): ...
    
class Foo(AbstarctFoo):
    def __init__(self, nome) -> None:
        super().__init__(nome)
    
    # @property
    # def nome(self):
    #     return self._nome
    
    # @nome.setter
    # def nome(self, nome):
    #     self._nome = nome

    @AbstarctFoo.nome.setter
    def nome(self, nome):
        self._nome = nome

f = Foo('Joao')
print(f.nome)
