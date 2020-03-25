from CursoPythonOtavioMiranda.Classes_Abstratas.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, cliente, agencia, conta, saldo, limite=1000):
        super().__init__(cliente, agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if not isinstance(valor,(int, float)):
            raise ValueError("O valor deve ser númerico")
        if (self._saldo + self._limite) < valor:
            print("O saldo é insuficiente")
            return

        self._saldo = self._saldo - valor
        self.extrato()

