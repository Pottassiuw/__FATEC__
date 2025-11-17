
#!/usr/bin/python -tt
# LISTA 1 - Exercícios Básicos

# A. divisivel_por_sete
# Dado um número n não negativo,
# retorna True se o número for divisível por 7
# ou se terminar com o dígito 7
# divisivel_por_sete(14) -> True
# divisivel_por_sete(23) -> False
# divisivel_por_sete(27) -> True
def divisivel_por_sete(n):
    n_f = str(n)
    if n%7==0 or n_f.endswith('7'):
        return True
    return False

# B. maior_unico
# Dados três números inteiros a, b, c
# retorna o maior número que aparece apenas uma vez
# se todos forem diferentes, retorna o maior
# se nenhum for único, retorna 0
# maior_unico(1, 2, 3) -> 3
# maior_unico(3, 2, 3) -> 2
# maior_unico(3, 3, 3) -> 0
def maior_unico(a, b, c):
    
    return


# C. soma_sem_cinco
# Soma três inteiros a, b, c
# Se aparecer um 5, ele não conta e todos os
# números à sua esquerda também não contam
# soma_sem_cinco(1, 2, 3) -> 6
# soma_sem_cinco(1, 5, 3) -> 3
# soma_sem_cinco(5, 2, 3) -> 0
def soma_sem_cinco(a, b, c):
    return


# D. triplica_char
# Retorna os caracteres da string original triplicados
# triplica_char('Oi') -> 'OOOiii'
# triplica_char('xyz') -> 'xxxyyyzzz'
def triplica_char(s):
    return


# E. conta_ba
# Conta o número de vezes que aparece a string 'ba'
# conta_ba('abc ba ho') -> 1
# conta_ba('baba') -> 2
# conta_ba('bababa') -> 3
def conta_ba(s):
    return


# F. rato_gato
# Verifica se aparece o mesmo número de vezes 'rato' e 'gato'
# rato_gato('ratogato') -> True
# rato_gato('ratorato') -> False
# rato_gato('1rato1gato') -> True
def rato_gato(s):
    return


# G. conta_java
# Conta quantas vezes aparece 'java'
# a letra 'v' pode ser trocada por outra qualquer
# assim 'jaba' ou 'jata' também são contadas
# conta_java('aaajavahhh') -> 1
# conta_java('javaxxjava') -> 2
# conta_java('jabaxxjata') -> 2
def conta_java(s):
    return


# H. comeca_termina
# As duas strings devem ser convertidas para minúsculo via lower()
# Depois disso verifique se a string a começa com b
# ou se a string b começa com a
# comeca_termina('Hello', 'hel') -> True
# comeca_termina('abc', 'xyz') -> False
def comeca_termina(a, b):
    return


# I. conta_multiplos_tres
# Conta os números múltiplos de 3 da lista
# conta_multiplos_tres([3, 6, 9, 10]) -> 3
# conta_multiplos_tres([1, 2, 4]) -> 0
def conta_multiplos_tres(nums):
    return


# J. soma7
# Retorna a soma dos números de uma lista
# 7 dá azar, você deverá ignorar o 7 e todos à sua direita
# soma7([1, 2, 2, 1]) -> 6
# soma7([1, 2, 2, 1, 7]) -> 6
# soma7([7, 1, 2, 3]) -> 0
def soma7(nums):
    return


# K. tem33
# Verifica se na lista aparecem dois 3 consecutivos
# tem33([1, 3, 3]) -> True
# tem33([1, 3, 1, 3]) -> False
# tem33([3, 1, 3]) -> False
def tem33(nums):
    return


# L. produto_na_lista
# Verifica se um número é produto de dois elementos distintos
# produto_na_lista(6, [1, 2, 3, 4]) -> True (2*3=6)
# produto_na_lista(10, [1, 2, 3, 4]) -> False
def produto_na_lista(n, lista):
    return


# M. pilha_livros
# Queremos montar uma pilha de livros de uma altura meta
# Temos livros finos (altura 2) e grossos (altura 7)
# Retorna True se for possível montar a pilha
# pilha_livros(4, 1, 15) -> True (4*2 + 1*7 = 15)
# pilha_livros(3, 1, 10) -> False
def pilha_livros(n_fino, n_grosso, meta):
    return


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))


def main():
    print('Divisivel_por_sete')
    test(divisivel_por_sete(14), True)
    test(divisivel_por_sete(23), False)
    test(divisivel_por_sete(27), True)
    test(divisivel_por_sete(7), True)
    test(divisivel_por_sete(21), True)

    print()
    print('Maior_unico')
    test(maior_unico(1, 2, 3), 3)
    test(maior_unico(3, 2, 3), 2)
    test(maior_unico(3, 3, 3), 0)
    test(maior_unico(5, 5, 2), 2)

    print()
    print('Soma_sem_cinco')
    test(soma_sem_cinco(1, 2, 3), 6)
    test(soma_sem_cinco(1, 5, 3), 3)
    test(soma_sem_cinco(5, 2, 3), 0)
    test(soma_sem_cinco(1, 2, 5), 3)

    print()
    print('Triplica_char')
    test(triplica_char('Oi'), 'OOOiii')
    test(triplica_char('xyz'), 'xxxyyyzzz')
    test(triplica_char('A'), 'AAA')

    print()
    print('Conta_ba')
    test(conta_ba('abc ba ho'), 1)
    test(conta_ba('baba'), 2)
    test(conta_ba('bababa'), 3)

    print()
    print('Rato_gato')
    test(rato_gato('ratogato'), True)
    test(rato_gato('ratorato'), False)
    test(rato_gato('1rato1gato'), True)

    print()
    print('Conta_java')
    test(conta_java('aaajavahhh'), 1)
    test(conta_java('javaxxjava'), 2)
    test(conta_java('jabaxxjata'), 2)

    print()
    print('Comeca_termina')
    test(comeca_termina('Hello', 'hel'), True)
    test(comeca_termina('abc', 'xyz'), False)
    test(comeca_termina('Python', 'py'), True)

    print()
    print('Conta_multiplos_tres')
    test(conta_multiplos_tres([3, 6, 9, 10]), 3)
    test(conta_multiplos_tres([1, 2, 4]), 0)
    test(conta_multiplos_tres([12, 15, 18]), 3)

    print()
    print('Soma7')
    test(soma7([1, 2, 2, 1]), 6)
    test(soma7([1, 2, 2, 1, 7]), 6)
    test(soma7([7, 1, 2, 3]), 0)

    print()
    print('Tem33')
    test(tem33([1, 3, 3]), True)
    test(tem33([1, 3, 1, 3]), False)
    test(tem33([3, 1, 3]), False)

    print()
    print('Produto_na_lista')
    test(produto_na_lista(6, [1, 2, 3, 4]), True)
    test(produto_na_lista(10, [1, 2, 3, 4]), False)
    test(produto_na_lista(12, [2, 3, 4, 5]), True)

    print()
    print('Pilha_livros')
    test(pilha_livros(4, 1, 15), True)
    test(pilha_livros(3, 1, 10), False)
    test(pilha_livros(10, 2, 34), True)



if __name__ == '__main__':
    main()
