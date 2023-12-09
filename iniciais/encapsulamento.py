"""
Em Python,  convenções:
    _ -> protect
    __ -> private
"""

class Pai:
    _pai = 'Pai'

    @classmethod
    def _metodo_protect(cls): 
        print('_metodo_protect')


class Filho(Pai):
    __filho = 'Filho'
    
    @classmethod
    def __metodo_private(cls): print('__metodo_private')

    @classmethod
    def biriri(cls): 
        return cls.__metodo_private()
    
    @classmethod
    def biriri2(cls): 
        return cls._metodo_protect()
    
    @classmethod
    def chamar_pai(cls):
        print(f"Pai:{cls._pai}, Filho:{cls.__filho}")
    

Filho.chamar_pai()
Filho.biriri()
Filho.biriri2()