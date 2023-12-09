"""
__dict__ Representa a instancia em dicionario, o mesmo pode ser editado
"""

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Joao', 19)
print(p1.__dict__) #Dicionario com {'atributo': valor}
print(vars(p1)) #Mesmo resultado que o de cima

print()

p1.__dict__['Nova_Chave'] = 'Novo_valor'
print(p1.__dict__)
p1.__dict__['nome'] = 'Maria' #Mudando 'Joao' para 'Maria'
print(vars(p1))
print(p1.nome) #Maria
print(p1.Nova_Chave) #Retorna 'Novo_Valor'

print()

dados = {'nome':'Gui', 'idade':10}
p2 = Pessoa(**dados) #Desempacotando dados/dicionario
print(vars(p2))