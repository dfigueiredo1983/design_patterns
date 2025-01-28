"""
O Padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""

from __future__ import annotations
from abc import ABC, abstractmethod

class Order:
    """ Context """

    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        print('Tentando executar pending()')
        self.state.pending()
        print('Estado atual: ', self.state)
        print()

    def approved(self) -> None:
        print('Tentando executar approved()')
        self.state.approved()
        print('Estado atual: ', self.state)
        print()

    def rejected(self) -> None:
        print('Tentando executar rejected()')
        self.state.rejected()
        print('Estado atual: ', self.state)
        print()

class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None:
        ...

    @abstractmethod
    def approved(self) -> None:
        ...

    @abstractmethod
    def rejected(self) -> None:
        ...

    def __str__(self) -> str:
        return f'{self.__class__.__name__}'
    

class PaymentPending(OrderState):
    def pending(self) -> None:
        print('Pagamento já pendente, não posso fazer nada.')

    def approved(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('Pagamento aprovado')

    def rejected(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado')

class PaymentApproved(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento pendente.')

    def approved(self) -> None:
        print('Pagamento já aprovado.')

    def rejected(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado.')

class PaymentRejected(OrderState):
    def pending(self) -> None:
        print('Pagamento recusado, não posso ir para pendente.')

    def approved(self) -> None:
        print('Pagamento recusado, não posso ir para aprovado.')

    def rejected(self) -> None:
        print('Pagamento recusado, não posso recusar novamente.')

if __name__ == '__main__':
    order = Order()
    order.pending()
    order.approved()
    order.rejected()
    order.pending()

