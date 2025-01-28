"""
Mediator é um padrão de projeto comportamental
que tem a intenção de definir um objeto que
encapsula a forma como um conjunto de objetos
interage. O Mediator promove o baixo acoplamento
ao evitar que os objetos se refiram uns aos
outros explicitamente e permite variar suas
interações independentemente.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Colleague(ABC):
    def __init__(self) -> None:
        self.name: str    

    @abstractmethod
    def broadcast(self, msg: str) -> None:
        ...

    @abstractmethod
    def direct(self, msg: str) -> None:
        ...

    
class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg: str) -> None:
        self.mediator.broadcast(self, msg)

    def send_direct(self, receiver: str, msg: str) -> None:
        self.mediator.direct(self, receiver, msg)

    def direct(self, msg: str) -> None:
        print(msg)

# Interface - Classe abstrata
class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, msg: str) -> None:
        ...

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        ...

# Concrete Mediator - Classe concreta
class Chatroom(Mediator):
    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []
    
    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, msg: str) -> None:
        if not self.is_colleague(colleague):
            return
        
        print(f'{colleague.name} disse: {msg}')
    
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        if not self.is_colleague(sender):
            return
    
        receiver_obj: List[Colleague] = [
            colleague for colleague in self.colleagues
            if colleague.name == receiver
        ]

        if not receiver_obj:
            return
        
        receiver_obj[0].direct(
            f'{sender.name} para {receiver_obj[0].name}: {msg}'
        )


if __name__ == '__main__':
    chat = Chatroom()

    Daniel = Person('Daniel', chat)
    Aline = Person('Aline', chat)
    Pedro = Person('Pedro', chat)
    Gabriel = Person('Gabriel', chat)
    Severino = Person('Severino', chat)
    Lazara = Person('Lazara', chat)

    chat.add(Daniel)
    chat.add(Aline)
    chat.add(Pedro)
    chat.add(Gabriel)
    chat.add(Severino)
    chat.add(Lazara)

    Daniel.broadcast('Olá grupo!')
    Aline.broadcast('Fala, beleza')

    Severino.broadcast('Eu também estou aqui. Boa tarde!')

    Daniel.send_direct('Pedro', 'Bom dia, meu filho amado.')
    Daniel.send_direct('Gabriel', 'Bom dia, meu lindão.')
    Daniel.send_direct('Aline', 'Bom dia, meu bem.')



