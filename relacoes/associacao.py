"""
Associação: um obejto é atributo de outro
"""
class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self): 
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class Ferramenta:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def escrever(self):
        print(f'{self.nome} escrevendo')
    
    def __str__(self) -> str:
        return self.nome

e1 = Escritor('Joao')
f1 = Ferramenta('Caneta')
e1.ferramenta = f1
print(e1.ferramenta)
e1.ferramenta.escrever()
