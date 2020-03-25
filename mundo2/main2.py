from classes2 import  CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()


p1 = Produto("Bicleta MTB", 2500.50)
p2 = Produto("Freio Alivio ", 234.00)
p3 = Produto("Trocador Alivio", 456.56)
p4 = Produto("Aro Vezan", 230.56)
p5 = Produto("Cambio Shimano Deore", 340.45)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p4)

carrinho.lista_produto()
carrinho.soma_total()

