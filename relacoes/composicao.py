"""
Relações entre classes: associação, agregação e composição
Composição é uma especialização da agregação.
Mas nela, quando o objeto "pai" for apagado, todas
as referências dos objetos filhos também são
apagadas.
"""

class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        """
            Dessa forma, temos a criacao de endereco através de Cliente, caso seja feita exclusao 
            de cliente da memória temos tambem a exclusao dos enderecos associados, efeito CASCADA
        """
        self.enderecos.append(Endereco(rua, numero))

        """
            Isso aqui demostra que tu inseriu um objeto endereco, ou seja, este objeto existe fora do contexto de cliente
            Contudo, caso cliente seja excluido os enderecos ainda vão existir
        """
        #self.enderecos.append(endereco:Endereco)

    
    def listar_endereco(self):
        print(*self.enderecos, sep='\n')

class Endereco:
    def __init__(self, rua, numero) -> None:
        self.rua = rua
        self.numero = numero
    
    def __str__(self) -> str:
        return f"{self.rua}, {self.numero}"

cliente = Cliente('Maria')
cliente.inserir_endereco('Rua Ernesto', '10')
cliente.inserir_endereco('Rua Tutu', '1')
cliente.listar_endereco()

#del cliente -> excluindo cliente da memoria