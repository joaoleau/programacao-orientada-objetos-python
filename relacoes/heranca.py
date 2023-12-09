#Herança já estudei anterirormente
class MinhaString(str):
    def upper(self):
        print('Minha upper')
        return super().upper()
    
string =  MinhaString('Joao')
print(string.upper())

print()


class A:
    def __init__(self, atributo_a) -> None:
        self.atributo_a = atributo_a

    def metodo(self):
        print('A')

class B(A):
    def __init__(self, atributo_b, atributo_a) -> None:
        super().__init__(atributo_a)
        self.atributo_b = atributo_b

    def metodo(self):
        print('B')

class C(B):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print('__init C')

    def metodo(self):
        super(B, self).metodo() #Chama super de B
        super(C, self).metodo() #Chama super de C

        #Mesmo resultado
        # B.metodo(self)
        # A.metodo(self)
        
        print('C')

    def __str__(self) -> str:
        return f'{self.atributo_b}, {self.atributo_a}'

c = C('B', 'A')
c.metodo()
print(c)

#Importante e INTERESSANTE
print(C.mro()) #mro -> Ordem de resolução do método
print(B.mro())