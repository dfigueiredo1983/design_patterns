"""
O padrão Observer tem a intenção de
definir uma dependência de um-para-muitos entre
objetos, de maneira que quando um objeto muda de
estado, todo os seus dependentes são notificados
e atualizados automaticamente.

Um observer é um objeto que gostaria de ser
informado, um observable (subject) é a entidade
que gera as informações.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Dict

class IObservable(ABC):
    """ Observable """

    @property # Getter
    @abstractmethod
    def state(self) -> Dict:
        ...

    @state.setter # Setter
    @abstractmethod
    def state(self, _state_update: Dict) -> None:
        ...

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None:
        ...

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None:
        ...

    @abstractmethod
    def notify_observers(self) -> None:
        ...

class WeatherStation(IObservable):
    """ Observable """

    def __init__(self):
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property # Getter
    def state(self) -> Dict:
        return self._state

    @state.setter # Setter
    def state(self, _state_update: Dict) -> None:
        new_state: Dict = {**self._state, **_state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer not in self._observers:
            return
        
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()
        print()




class IObserver(ABC):
    @abstractmethod
    def update(self) -> None:
        ...

class Observer(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto {observable_name} '
              f'acabou de ser atualizado. => {self.observable.state}')

class Smartphone(Observer):
    ...

class Tablet(Observer):
    ...

if __name__ == '__main__':
    weather_station = WeatherStation()
    smartphone_1 = Smartphone('Xiaomi', weather_station)
    smartphone_2 = Smartphone('Apple', weather_station)

    weather_station.add_observer(smartphone_1)
    weather_station.add_observer(smartphone_2)

    weather_station.state = {'temperature': 30}
    weather_station.state = {'pressure': '1 atm'}

    weather_station.remove_observer(smartphone_1)

    weather_station.reset_state()

    tablet_1 = Tablet('Samsung tab A10', weather_station)
    weather_station.add_observer(tablet_1)

    weather_station.state = {'Velocit': '120 km/h'}





