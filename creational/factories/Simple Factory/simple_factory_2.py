"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID
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

class VeiculoFactory:

    def __init__(self, tipo: str):
        self.carro = self.get_carro(tipo)

    @staticmethod # não preciso instânciar a classe 
    # método de fábrica - factory method
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

    def buscar_cliente(self):
        self.carro.buscar_cliente()


if __name__ == '__main__':
    from random import choice
    carros_disponiveis = ['luxo', 'popular', 'moto_luxo', 'moto_popular']

    for i in range(10):
        veiculo = VeiculoFactory(choice(carros_disponiveis))
        veiculo.buscar_cliente()

