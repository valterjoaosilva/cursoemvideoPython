from vendas.formatador_preço import formatar

def aumento(valor, percentual, formata=False):
    a = valor + (valor * percentual / 100)
    if formata:
        return formatar.formatar(a)
    else:
        return a

def desconto(valor, percental, formata=False):
    d = valor - (valor * percental / 100)
    if formata:
        return formatar.formatar(d)
    else:
        return d


