"""
O Padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict

class Sound:
    def __init__(self) -> None:
        self.mode: PlayMode = RadioMode(self)
        self.playing = 0
        self.store_playing: Dict = {}
    
    def change_mode(self, mode: PlayMode) -> None:
        # salvando o estado atual no dicionário com a chave
        # sendo o nome do tipo de PlayMode (RadioMode, MusicMode)
        current_mode_name = type(self.mode).__name__
        # print('Current mode name: ', current_mode_name)
        # print('Currente mode class', self.mode.__class__.__name__)
        # print('Type: ', type(self.mode))
        self.store_playing[current_mode_name] = self.playing

        # Recuperando os dados salvos no dicionário, se existir uma entrada
        new_mode_name = type(mode).__name__
        self.playing = self.store_playing.get(new_mode_name, 0)

        # self.playing = 0
        self.mode = mode

    def press_next(self) -> None:
        self.mode.press_next()
        print(self)

    def press_prev(self) -> None:
        self.mode.press_prev()
        print(self)

    def __str__(self) -> str:
        return f'{self.playing}'
    


class PlayMode(ABC):
    def __init__(self, sound: Sound) -> None:
        self.sound = sound

    @abstractmethod
    def press_next(self) -> None:
        ...

    @abstractmethod
    def press_prev(self) -> None:
        ...

class RadioMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 1000

    def press_prev(self) -> None:
        self.sound.playing -= 1000 if self.sound.playing > 0 else 0

class MusicMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 1

    def press_prev(self) -> None:
        self.sound.playing -= 1 if self.sound.playing > 0 else 0

if __name__ == '__main__':
    sound = Sound()
    radio = RadioMode(sound)
    music = MusicMode(sound)

    print('Rádio')
    radio.press_next()
    print(radio.sound.playing)

    sound.change_mode(music)
    print('Music')
    music.press_next()
    print(music.sound.playing)

    sound.change_mode(radio)
    print('Rádio')
    radio.press_next()
    print(radio.sound.playing)

    sound.change_mode(music)
    print('Music')
    music.press_next()
    print(music.sound.playing)

    sound.change_mode(radio)
    print('Rádio')
    radio.press_next()
    print(radio.sound.playing)

    sound.change_mode(music)
    print('Music')
    music.press_next()
    print(music.sound.playing)

    sound.change_mode(radio)
    print('Rádio')
    radio.press_next()
    print(radio.sound.playing)

    sound.change_mode(music)
    print('Music')
    music.press_next()
    print(music.sound.playing)

    sound.change_mode(radio)
    print('Rádio')
    radio.press_next()
    print(radio.sound.playing)


