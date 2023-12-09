"""
São métodos estáticos, apenas uma função dentro da classe, não precisa de instancia
Obs: Por não usar 'cls' e nem 'self' o mesmo não possui acesso a estes dados
"""

class Pessoa:
    def __init__(self, nome=None, idade=None) -> None:
        self.nome = nome
        self.idade = idade

    def gritar(self):
        print(f'Veemmm aquiiiiiii {self.nome}!!!') #Repare que acessei o valor de nome
    
    @staticmethod
    def funcao_estatica():
        print('blabla')

p1 = Pessoa('Joao', 19)
Pessoa.gritar(p1)
Pessoa.funcao_estatica()