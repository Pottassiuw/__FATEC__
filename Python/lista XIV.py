#Conceitos de funções (yield e lambda)
# def f ():
#     yield 'abacate'
#     yield 42
#     yield 'fim'

# x = f()

# print(next(x))

# print(next(x))

#variaveis globais
a = 42
def f():
    global a
    a = 13
    print(a)
print(a)
f()
print(a)
