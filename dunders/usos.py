class Ponto:
    def __init__(self, x, y, z='String') -> None:
        self.x = x
        self.y = y
        self.z = z


    def __add__(self, other):
        novo_x = other.x + self.x
        novo_y = other.y + self.y
        return Ponto(novo_x, novo_y)

    def __str__(self) -> str:
        return f'(x:{self.x},y:{self.y})'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} = (x:{self.x!r},y:{self.y!r}, z:{self.z!r})'

p1 = Ponto(12,2)
p2 = Ponto(0,10)

print(p1)
print(repr(p1)) # == p1!r
print(p1+p2)