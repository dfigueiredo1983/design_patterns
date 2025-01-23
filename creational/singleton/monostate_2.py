"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""

from typing import Dict

class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        # print(params)
        return f'{self.__class__.__name__}({params})'
    
    def __repr__(self):
        return self.__str__()

class MonoState(StringReprMixin):
    _state: Dict = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, nome=None, sobrenome=None):
        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome

class A(MonoState):
    ...

if __name__ == '__main__':
    mono_state_1 = MonoState(nome='Daniel', sobrenome='Figueiredo')

    print(mono_state_1)

    mono_state_2 = MonoState()
    print(mono_state_2)

    mono_state_3 = A()
    print(mono_state_3)

# class A(StringReprMixin):
#     def __init__(self, nome):
#         self.x = 10
#         self.y = 20
#         self.nome = nome


# a = A('Daniel')
# print(a.__dict__)

# print(a)

# # a.__dict__['nome'] = 'Daniel Figueiredo'
# # print(a.__dict__)

# # a.__dict__['idade'] = 41
# # print(a.__dict__)

# # a.__dict__.pop('x')
# # print(a.__dict__)

# # a.__dict__.popitem()
# # print(a.__dict__)
