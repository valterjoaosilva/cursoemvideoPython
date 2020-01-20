minha_String = "valter joão da silva junior"
c = 0
nova_String = ''
while c < len(minha_String):
    if minha_String[c] == 'r':
        nova_String = nova_String + minha_String[c].upper()
    else:
        nova_String = nova_String + minha_String[c]

    c += 1
print(f'{nova_String}')

print(f'{"="*40}')
c = 0
contagem_Atual = 0
letra = ''
while c < len(minha_String):
    qtd_vezesLetra = minha_String.count(minha_String[c])

    if contagem_Atual < qtd_vezesLetra and minha_String[c].strip():
        letra = minha_String[c]
        contagem_Atual = qtd_vezesLetra
    c += 1
print(f'{letra} = {contagem_Atual}')




