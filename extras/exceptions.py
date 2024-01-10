class MyError(Exception):
    ...

class OutroError(Exception):
    ...

def levantar():
    exception_ = MyError("A msg do meu erro")
    raise exception_

try:
    1/0
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    exception_ = OutroError("Relançar erro")
    raise exception_ from error #Lançando outra excecao causada por outra excecao