from CursoPythonOtavioMiranda.Classes_Abstratas.poupanca import ContaPoupança
from CursoPythonOtavioMiranda.Classes_Abstratas.contacorrente import ContaCorrente
from CursoPythonOtavioMiranda.Classes_Abstratas.contaInvestimento import ContaInvestimento

cp = ContaPoupança("Valter João", 2234, 234556, 0)
cp.depositar(120.00)
cp.sacar(110.00)
cp.sacar(24.00)
cp.extrato()

print("#######################")

cc = ContaCorrente("Valter João", 4455, 4453, 0, limite=1000)
cc.depositar(200.00)
cc.sacar(450.00)
cc.sacar(790.00)
cc.depositar(1250.00)

print("#############################")
ci = ContaInvestimento("valter", 3344, 4355, 0)
ci.depositar(1200)
ci.cdb()
ci.sacar(1200)
ci.cdi()



