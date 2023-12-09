# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor
    
    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, motor):
        self._fabricante = motor

    def __str__(self) -> str:
        return f'{self.nome}, {self.motor}, {self.fabricante}'

class Motor:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def __str__(self) -> str:
        return self.nome

class Fabricante:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def __str__(self) -> str:
        return self.nome
    
motor = Motor('2Jz')
fabricante = Fabricante('Toyota')

c1 = Carro('Supra')
c1.fabricante = fabricante
c1.motor = motor

print(c1)