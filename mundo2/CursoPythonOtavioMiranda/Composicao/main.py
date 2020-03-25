from CursoPythonOtavioMiranda.Composicao.classes import Cliente

cliente1 = Cliente("Valter", 51)
cliente1.inserir_endereco("Blumenau", "SC")

cliente2 = Cliente("Samira", 46)
cliente2.inserir_endereco("Blumenau", "SC")

cliente3 = Cliente("Pedro", 16)
cliente3.inserir_endereco("Blumenau", "SC")

print(cliente2.nome)
cliente2.lista_endereco()

print(f'O cliente 2 é: {cliente2.nome}, O Cliente 3 é: {cliente3.nome}')





