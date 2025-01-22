"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O 
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""
from abc import ABC, abstractmethod

# Especializar a classe veículo
class Veiculo(ABC):
    @abstractmethod # Obrigado a todas as classes derivadas a implementar esse método
    def buscar_cliente(self) -> None:
        print('Método da classe base')
        ...

class CarroLuxo(Veiculo):
    def buscar_cliente(self):
        print('Carro de luxo está buscando o cliente...')
        # return super().buscar_cliente()

class CarroPopular(Veiculo):
    def buscar_cliente(self):
        print('Carro popular está buscando o cliente...')
        # return super().buscar_cliente()

class MotoLuxo(Veiculo):
    def buscar_cliente(self):
        print('Moto de luxo está buscando o cliente...')
        # return super().buscar_cliente()

class MotoPopular(Veiculo):
    def buscar_cliente(self):
        print('Moto popular está buscando o cliente...')
        # return super().buscar_cliente()

class VeiculoFactory(ABC):
    def __init__(self, tipo: str):
        self.carro = self.get_carro(tipo)

    @staticmethod # não preciso instânciar a classe 
    @abstractmethod # obriga as classes herdeiras a implementar esse método
    def get_carro(tipo: str) -> Veiculo:
        ...

    def buscar_cliente(self):
        self.carro.buscar_cliente()

class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod # não preciso instânciar a classe 
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        if tipo == 'moto_popular':
            return MotoPopular()
        assert 0, 'Veículo não existe.'

class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod # não preciso instânciar a classe 
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veículo não existe.'


if __name__ == '__main__':
    from random import choice
    veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto_luxo', 'moto_popular']
    veiculos_disponiveis_zona_sul = ['popular']

    for i in range(10):
        veiculo_zona_sul = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte))
        veiculo_zona_sul.buscar_cliente()

    print()

    for i in range(10):
        veiculo_zona_norte = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        veiculo_zona_norte.buscar_cliente()



