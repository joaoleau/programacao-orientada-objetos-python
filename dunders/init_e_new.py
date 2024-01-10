class A:
    def __new__(cls, *args, **kwargs): #New cria a instancia(self) e passa para init, ou seja, new vem antes de init
        print('Antes de criar a instancia')
        return super().__new__(cls)

    def __init__(self, x) -> None:
        print('Oi')
        self.x = x

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} - {self.x}'
    
print(A('sdad'))
