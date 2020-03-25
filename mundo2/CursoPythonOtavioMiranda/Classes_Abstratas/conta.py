from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, cliente, agencia, conta, saldo):
        self._cliente = cliente
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def cliente(self):
        return self._cliente

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor precisa ser númerico")
        self._saldo = valor
        self.extrato()

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor precisa ser númerico")
        self._saldo = self.saldo + valor
        self.extrato()

    def extrato(self):
        print(f' Cliente: {self._cliente} - agência: {self._agencia} - conta: {self._conta} - Saldo: R${self._saldo}')


    @abstractmethod
    def sacar(self):
        pass

