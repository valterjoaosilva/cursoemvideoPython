from CursoPythonOtavioMiranda.Classes_Abstratas.conta import Conta


class ContaInvestimento(Conta):
    def cdb(self, juros=1.2):
        if not isinstance(juros, (int, float)):
            raise ValueError("Juros e valor devem ser númericos")
        self._saldo = ((self._saldo * juros)/100) + self._saldo
        self.extrato()

    def cdi(self, juros=1.5):
        if not isinstance(juros,(int, float)):
            raise ValueError("Juros tem que ser númerico")
        self._saldo = ((self._saldo * juros)/100) + self._saldo
        self.extrato()


    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor tem que ser númerico")
        if self._saldo < valor:
            print("saldo insuficiente")
        self._saldo = self._saldo - valor
        self.extrato()


