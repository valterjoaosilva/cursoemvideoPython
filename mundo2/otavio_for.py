
for n in range(0, 100, 1):

    print(n)
texto = 'python'
nova_String = ''
for l in texto:
    if l in 'th':
        nova_String += l.upper()
    else:
        nova_String += l
print(nova_String)
