
"""
São métodos que não precisam receber instancia, são chamados diretamente através da classe.
Obs: cls é usado como self, porém de vez tratar instancia trata a classe;
    Primeiro parâmetro sempre 'cls'
    Podem ser usados para serem factories methods
"""
class Pessoa:
    def __init__(self, nome=None, idade=None) -> None:
        self.nome = nome
        self.idade = idade

    def andar(self):
        print('Andando')

    @classmethod
    def metodo_de_classe(cls):
        print(f"Metodo de classe", end='\n\n')

    @classmethod
    def criar_pessoa_100_anos(cls, nome): #Metodo Fabrica
        return cls(nome, 100) 
    
# Pessoa.andar() //Da erro
Pessoa.metodo_de_classe()

p1 = Pessoa()
p2 = Pessoa.criar_pessoa_100_anos('Maria')
print(p2.nome)
print(p1.nome)