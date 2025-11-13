print('\n\n=== LISTA 4 - LISTAS ===\n')


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

# A. inicio_fim_igual
# Conta strings com tamanho >= 2 onde primeiro == último char
def inicio_fim_igual(words):
    return


# B. y_primeiro
# Strings que começam com 'y' vêm primeiro, todas ordenadas
def y_primeiro(words):
    return


# C. ordena_ultimo
# Ordena tuplas pelo último elemento
def ultimo_elemento(tupla):
    return

def ordena_ultimo(tuples):
    return

def main():
    print('Inicio_fim_igual')
    test(inicio_fim_igual(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(inicio_fim_igual(['', 'x', 'xy', 'xyx', 'xx']), 2)

    print()
    print('Y_primeiro')
    test(y_primeiro(['bbb', 'ccc', 'yxx', 'yzz', 'yaa']),
         ['yaa', 'yxx', 'yzz', 'bbb', 'ccc'])

    print()
    print('Ordena_ultimo')
    test(ordena_ultimo([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(ordena_ultimo([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])


if __name__ == '__main__':
    main()