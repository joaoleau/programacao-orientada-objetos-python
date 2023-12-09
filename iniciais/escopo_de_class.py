class Animal:
    nome = 'animal' #Comporta-se como uma variavel, ATRIBUTO DE CLASSE

print(Animal.nome, end='\n\n')


class Animal2:
    def __init__(tutu, nome) -> None:
        tutu.nome = nome

Animal2.nome = 'Jacare'
print(Animal2.nome, end='\n\n')


class Animal3:
    def __init__(kkkk, nome) -> None:
        kkkk.nome = nome

# print(Animal3.nome) //Bate o erro


class Animal4(Animal):
    pass

print(Animal4.nome) #'animal'
Animal4.nome = 'animal4'
print(Animal4.nome, end='\n\n') #'animal4'


class Animal5(Animal):
    def __init__(self, tipo) -> None:
        self.nome = tipo
        #self.tipo = tipo //Caso chame dog.nome retorno 'animal' e dai nao sobrescrito, pois primeiro é chamado atributos da instancia e depois da classe

dog = Animal5('cachorro')
print(dog.nome) #'cachorro' ou 'animal' ^^
print(Animal5.nome) #'animal'