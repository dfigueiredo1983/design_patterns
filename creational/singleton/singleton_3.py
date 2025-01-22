"""
O Singleton tem a intenção de garantir que uma classe tenha somente
uma instância e fornece um ponto global de acesso para a mesma.

When discussing which patterns to drop, we found
that we still love them all.
(Not really—I'm in favor of dropping Singleton.
Its use is almost always a design smell.)
- Erich Gamma, em entrevista para informIT
http://www.informit.com/articles/article.aspx?p=1404056
"""
# class Meta(type):
#     def __call__(self, *args, **kwargs):
#         print('CALL EXECUTADO')
#         return super().__call__(*args, **kwargs)

# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('NEW EXECUTADO')
#         return super().__new__(cls)


#     def __init__(self, nome):
#         print('INIT EXECUTADO')
#         self.nome = nome

#     def __call__(self, *args, **kwds):
#         print('Call chamado')

# pessoa = Pessoa('Daniel')
# print(pessoa.nome)

from typing import Dict

class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
# class AppSettings:
    def __init__(self):
        self.tema = 'O tema escuro'
        self.font = '18px'

if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    print(as1.tema)

    as2 = AppSettings()
    as3 = AppSettings()
    print(as2.tema)
    print(as3.tema)

    print(as1 == as2)
    print(as1 == as3)

