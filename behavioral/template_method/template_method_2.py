"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""

from abc import ABC, abstractmethod

class Pizza(ABC):
    """ Classe abstrata """

    def prepare(self) -> None:
        """ Template method """
        self.hook_before_add_ingredients()
        self.add_ingredients() # Abstract
        self.hook_after_add_ingredients()
        self.cook() # Abstract
        self.cut() # Concrete
        self.serve() # Concrete

    def hook_before_add_ingredients(self) -> None:
        ...

    def hook_after_add_ingredients(self) -> None:
        ...

    @abstractmethod
    def add_ingredients(self) -> None:
        ...

    @abstractmethod
    def cook(self) -> None:
        ...

    def cut(self) -> None:
        print(f'{self.__class__.__name__}. CORTANDO A PIZZA')

    def serve(self):
        print(f'{self.__class__.__name__}. SERVINDO A PIZZA')


class HomemadePizza(Pizza):
    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}')
        print('Add ovo cozido')
        print('Add pimentão')
        print('Add cebola')
        print('Add mussarela')
        print('Add presunto')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}')
        print('Pré assando a massa por 3 minutos no forno a lenha')
        print('Assando a massa até ficar dourada')

class VeganPizza(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}. Manipulação especial para uma pizza vegana.')
        print(f'Lavando ingredientes')

    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}')
        print('Add molho de tomate')
        print('Add pimentão')
        print('Add cebola')
        print('Add mussarela vegana')
        print('Add presunto vegano')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}')
        print('Pré assando a massa por 3 minutos no forno a lenha')
        print('Assando a massa até ficar dourada')

homemadePizza = HomemadePizza()
homemadePizza.prepare()

veganPizza = VeganPizza()
veganPizza.prepare()



