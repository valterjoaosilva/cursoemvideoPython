'''
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
print(ask_ok("input yes or no"))

i = 5
def f(arg=i):
    print(arg)
i = 6
f()
#imprime o valor passado antes da função neste caso 5. Os valor são avaliados no ponto de definição.
# o valor é avaliado apenas uma vez, por isso não muda quando é alterado após a função.

def f(a, L=[]):
    L.append(a)
    print(L)
    return L

f(23)
f(12)
f(34)
'''
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    print(L)
    return L
f(23)
f(34)
f(56)





