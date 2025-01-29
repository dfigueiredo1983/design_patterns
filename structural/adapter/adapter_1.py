"""
Adapter é um padrão de projeto estrutural que
tem a intenção de permitir que duas classes
que seriam incompatíveis trabalhem em conjunto
através de um "adaptador".
"""
from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self):
        ...

    @abstractmethod
    def down(self):
        ...
    @abstractmethod
    def left(self):
        ...

    @abstractmethod
    def right(self):
        ...

class Control(IControl):
    def top(self):
        print('Movendo para cima...')

    def down(self):
        print('Movendo para baixo...')

    def left(self):
        print('Movendo para a esquerda...')

    def right(self):
        print('Movendo para a direita...')

class NewControl:
    def move_top(self):
        print('NewControl: Movendo para cima...')

    def move_down(self):
        print('NewControl: Movendo para baixo...')

    def move_left(self):
        print('NewControl: Movendo para a esquerda...')

    def move_right(self):
        print('NewControl: Movendo para a direita...')

class ControlAdapter:
    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self):
        self.new_control.move_top()

    def down(self):
        self.new_control.move_down()

    def left(self):
        self.new_control.move_left()

    def right(self):
        self.new_control.move_right()


if __name__ == '__main__':
    new_control = NewControl()
    controle_adapter = ControlAdapter(new_control)
    
    controle_adapter.down()
    controle_adapter.top()
    controle_adapter.left()
    controle_adapter.right()

    control = Control()
    control.down()
    control.top()
    control.left()
    control.right()
    



