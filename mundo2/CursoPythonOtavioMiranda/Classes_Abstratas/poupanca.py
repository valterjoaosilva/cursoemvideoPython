from CursoPythonOtavioMiranda.Classes_Abstratas.conta import Conta

class ContaPoupança(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor precisa ser númerico")
        if self._saldo < valor:
            print("O saldo em sua conta é insuficiente")
            return

        self._saldo = self._saldo - valor
        self.extrato()

