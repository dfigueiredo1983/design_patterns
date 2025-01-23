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

class MonoStateSimple(StringReprMixin):
    _state: Dict = {
        'x': 10,
        'y': 20,
    }

    def __init__(self, nome=None, sobrenome=None):
        self.__dict__ = self._state
        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome

if __name__ == '__main__':
    mono_state_1 = MonoStateSimple(nome='Daniel', sobrenome='Figueiredo')

    print(mono_state_1)

    mono_state_2 = MonoStateSimple()
    print(mono_state_2)



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
