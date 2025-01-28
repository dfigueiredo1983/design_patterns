# O CÓDIGO A SEGUIR NÃO APRESENTA O PADRÃO DE PROJETO STATE
# É UM EXEMPLO DO QUE O PADRÃO TENTA SOLUCIONAR

from __future__ import annotations
from enum import Enum, auto

class Payment(Enum):
    """
    Definimos um enum com as opções de estado
    que o nosso objeto Order pode ter
    """
    Pending = auto()
    Approve = auto()
    Reject = auto()

    def __str__(self):
        """O retorno aqui será o nome da classe (Pyment)
        mais o nome do membro. Ex.: PaymentApprove
        """
        return f'{self.__class__.__name__}{self.name}'

class Order:
    def __init__(self) -> None:
        self.state: Payment = Payment.Pending

    def change_state(self, state: Payment):
        """
        O CÓDIGO A SEGUIR NÃO APRESENTA O PADRÃO DE PROJETO STATE
        É UM EXEMPLO DO QUE O PADRÃO TENTA SOLUCIONAR.
        """

        # Pending
        if self.state == Payment.Pending and state == Payment.Pending:
            print('Pagamento já pendente, não vou mover para pendente.')
        elif self.state == Payment.Pending and state == Payment.Approve:
            self.state = Payment.Approve
            print('Pagamento aprovado')
        elif self.state == Payment.Pending and state == Payment.Reject:
            self.state = Payment.Reject
            print('Pagamento recusado')

        # Approve
        if self.state == Payment.Approve and state == Payment.Approve:
            print('Pagamento já aprovado, não vou aprovar para pendente.')
        elif self.state == Payment.Approve and state == Payment.Reject:
            self.state = Payment.Reject
            print('Pagamento recusado')
        elif self.state == Payment.Approve and state == Payment.Pending:
            self.state = Payment.Approve
            print('Pagamento pendente')

        # Reject
        if self.state == Payment.Reject and state == Payment.Approve:
            print('Pagamento recusado, não posso aprovar.')
        elif self.state == Payment.Approve and state == Payment.Reject:
            print('Pagamento recusado, não posso recusar novamente.')
        elif self.state == Payment.Reject and state == Payment.Pending:
            print('Pagamento recusado, não posso mover para pendente')

        print(f'Estado atual: {self.state}')
        print()

    def pending(self) -> None:
        print('Tentando executar pending(Payment.Pending)')
        self.change_state(Payment.Pending)

    def Approve(self) -> None:
        print('Tentando executar approve(Payment.Approve)')
        self.change_state(Payment.Approve)

    def Reject(self) -> None:
        print('Tentando executar reject(Payment.Reject)')
        self.change_state(Payment.Reject)


if __name__ == '__main__':
    order_1 = Order()

    order_1.Approve()
    order_1.Approve()
    order_1.Reject()
    order_1.Approve()
    order_1.pending()
    order_1.Approve()

