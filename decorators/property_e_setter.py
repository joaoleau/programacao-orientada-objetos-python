"""
@property é uma propriedade do objeto, é um método qeu se comporta como atributo
Pode ser usado para:
    - como getter
    - p/ evitar quebrar código cliente (Código cliente - é o código que usa seu código)
    - p/ habilitar setter
    - p/ executar ações ao obter um atributo


@atributo.setter
Usado para definir valores a atributos
Já é chamado dentro da '__init__' em self.atributo

"""

class Caneta:
    def __init__(self, cor) -> None:
        self.cor = cor #Nesta parte o 'self.cor' já chama o setter e daí é feita a lógica

    # def getter_cor_padrao(self):
    #     return self.cor
    
    # def setter_cor_padrao(self, cor) -> None:
    #     self.cor = cor
    
    @property
    def cor(self):
        print('CAIU NO GETTER')
        return self._cor
    
    @cor.setter
    def cor(self, cor):
        print('CAIU NO SETTER')
        #Aqui pode fazer a logica para o setter de cor
        self._cor = cor #'_cor' é encapsulamento, nesta linha é criado um novo atributo _cor (protect) que recebe o msm valor de cor

    def __str__(self) -> str:
        return f"{self.cor}"
    

# c1 = Caneta('Azul')
# print(c1.getter_cor_padrao())
# c1.setter_cor_padrao('Amarelo')
# print(c1)

c2 = Caneta('Verde') #Cai no setter, por isso é um metodo que se comporta como atributo
c2.cor = 'Rosa' #Cai no getter, por isso é um metodo que se comporta como atributo
print(c2.cor)