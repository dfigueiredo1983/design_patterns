"""
GoF - Memento é um padrão de projeto comportamental
que tem a intenção de permitir que você salve e restaure
um estado anterior de um objeto originator sem revelar os
detalhes da sua implementação e sem violar o encapsulamento.

Originator é o objeto que deseja salvar seu estado.
Memento é usado para salvar o estado do Originator.
Caretaker é usado para armazenar mementos.
Caretaker também é usado com o Padrão Command.
"""
from __future__ import annotations
from typing import Dict, List
from copy  import deepcopy

class Memento:
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        super().__setattr__('_state', state)
        # object.__setattr__(self, '_state', state)

    def get_state(self) -> Dict:
        return self._state

    # torna essa classe imutável
    def __setattr__(self, name, value):
        raise AttributeError('Sorry, I am immutable.')

class ImageEditor:
    def __init__(self, name:str, width: int, height: int) -> None:
        self.name = name
        self.width = width
        self.height = height
    
    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore_state(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'
    
class Carataker:
    def __init__(self, originator: ImageEditor) -> None:
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        if not self._mementos:
            return
        self._originator.restore_state(self._mementos.pop())

    def list_mementos(self) -> List[Memento]:
        print(type(self._mementos))
        for memento in self._mementos:
            print(memento.get_state())
        return self._mementos
    
if __name__ == '__main__':
    imageEditor = ImageEditor('Foto_1.jpg', 100, 100)
    carataker = Carataker(imageEditor)
    carataker.backup()
    carataker.list_mementos()

    imageEditor.name = 'Foto_2.jgp'
    imageEditor.width = 200
    imageEditor.height = 200
    carataker.backup()
    carataker.list_mementos()

    imageEditor.name = 'Foto_3.jgp'
    imageEditor.width = 300
    imageEditor.height = 300
    carataker.backup()
    carataker.list_mementos()

    imageEditor.name = 'Foto_4.jgp'
    imageEditor.width = 400
    imageEditor.height = 400
    carataker.backup()
    carataker.list_mementos()

    imageEditor.name = 'Foto_5.jgp'
    imageEditor.width = 500
    imageEditor.height = 500

    print(f'Estado atual: {imageEditor}')
    carataker.restore()
    print(f'Estado atual: {imageEditor}')
    carataker.restore()
    print(f'Estado atual: {imageEditor}')
    carataker.restore()
    print(f'Estado atual: {imageEditor}')
    carataker.restore()
    print(f'Estado atual: {imageEditor}')
    carataker.restore()
    print(f'Estado atual: {imageEditor}')
