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

class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation_1()
        self.base_class_method()
        self.operation_2()

    def hook(self):
        ...

    def base_class_method(self):
        print('OLÁ EU SOU DA CLASSE ABSTRATA E SEREI EXECUTADO TAMBÉM.')

    @abstractmethod
    def operation_1(self):
        ...

    @abstractmethod
    def operation_2(self):
        ...

class ConcreteCLass1(Abstract):
    def hook(self):
        print('EXECUTANDO O HOOK DA CLASSE ABSTRATA')

    def operation_1(self):
        print('Operação 1 concluída') 

    def operation_2(self):
        print('Operação 2 concluída') 

class ConcreteCLass2(Abstract):
    def operation_1(self):
        print('Operação 1 concluída da classe concreta 2') 

    def operation_2(self):
        print('Operação 2 concluída da classe concreta 2') 

if __name__ == '__main__':
    concrete_1 = ConcreteCLass1()
    concrete_1.template_method()

    print()

    concrete_2 = ConcreteCLass2()
    concrete_2.template_method()




