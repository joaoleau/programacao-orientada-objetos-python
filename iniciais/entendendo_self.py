
# 'self' é apenas uma convenção!!!!
class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome

    def buzinar(self) -> str:
        return 'bi bi'

    def __repr__(self) -> str:
        return self.nome

class Moto:
    def __init__(abc, nome) -> None:
        abc.nome = nome

    def andar(self) -> None:
        print(f"{self.nome} esta andando")
    
    def andar2(abc) -> None:
        print(f"{abc.nome} esta andando")

    @staticmethod
    def andar3() -> None:
        print('Andando "static"')

    def __repr__(jaja) -> str:
        return jaja.nome

fusca = Carro('Fusca')
print(fusca, end='\n\n')

hornet = Moto('hornet')
"""
    Moto.andar() -> andar nao sendo 'static' resulta em erro
    Porém é possivel chamar 'andar' passando como parametro o objeto:
"""
Moto.andar(hornet) #Quando voce esta usando 'self' significa usar uma instancia
hornet.andar()

Moto.andar3()