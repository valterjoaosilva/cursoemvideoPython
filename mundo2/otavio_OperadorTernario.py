'''
Operador Ternario

'''

logged_usario = False

if logged_usario:
    msg = "Usuario logado"
else:
    msg = "Usuário não está logado"

print(msg)

print("*"*40)
print("Operador Ternario")
logged_usario = True
msg = "Usuario logado" if logged_usario else 'Usuário não logado'
print(msg)