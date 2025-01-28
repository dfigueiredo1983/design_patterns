"""
Chain of responsibility (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# Implementando com funções
class Handler(ABC):
    def __init__(self) -> None:
        self.sucessor: Handler

    @abstractmethod
    def handler(self, letter: str) -> str:
        ...

class Handler_ABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters: List[str] = ['A', 'B', 'C']
        self.sucessor = sucessor
    
    def handler(self, letter: str) -> str:
        if letter in self.letters:
            return f'Eu {self.__class__.__name__} consigo tratar o {letter}'
        
        return self.sucessor.handler(letter)

class Handler_DEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters: List[str] = ['D', 'E', 'F']
        self.sucessor = sucessor
    
    def handler(self, letter: str) -> str:
        if letter in self.letters:
            return f'Eu {self.__class__.__name__} consigo tratar o {letter}'
        
        return self.sucessor.handler(letter)

class Handler_GHI(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters: List[str] = ['G', 'H', 'I']
        self.sucessor = sucessor
    
    def handler(self, letter: str) -> str:
        if letter in self.letters:
            return f'Eu {self.__class__.__name__} consigo tratar o {letter}'
        
        return self.sucessor.handler(letter)

class HandlerUnsolver(Handler):
    def handler(self, letter: str) -> str:
        return f'Eu {self.__class__.__name__} não consigo tratar o {letter}'
        
if __name__ == '__main__':
    handler_unsolver = HandlerUnsolver()
    handler_GHI = Handler_GHI(handler_unsolver)
    handler_DEF = Handler_DEF(handler_GHI)
    handler_ABC = Handler_ABC(handler_DEF)

    print(handler_ABC.handler('A'))
    print(handler_ABC.handler('B'))
    print(handler_ABC.handler('C'))
    print(handler_ABC.handler('D'))
    print(handler_ABC.handler('E'))
    print(handler_ABC.handler('F'))
    print(handler_ABC.handler('G'))
    print(handler_ABC.handler('H'))
    print(handler_ABC.handler('I'))
    print(handler_ABC.handler('J'))
    print(handler_ABC.handler('K'))
    print(handler_ABC.handler('L'))
    print(handler_ABC.handler('M'))

    