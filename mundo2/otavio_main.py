import vendas.calc_preco
from vendas import calc_preco
from vendas.calc_preco import aumento, desconto
from vendas.formatador_preço.formatar import formatar

preço_camisa = 50.00

preço_calça = 456.78

preço_jaqueta = 678.56

preço = 57.45


novo_preço_camisa = vendas.calc_preco.aumento(preço_camisa, 15, formata=True)
print(novo_preço_camisa)

novo_preço_calça = calc_preco.desconto(preço_calça, 5.2, formata=True)
print(novo_preço_calça)

novo_preço_jaqueta = aumento(preço_jaqueta, 2.5, formata=True)
print(novo_preço_jaqueta)

print(formatar(preço))



