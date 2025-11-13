print('\n\n=== LISTA 3 - STRINGS AVANÇADAS ===\n')

def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

# G. gerundio
# Se string tem pelo menos 4 caracteres, adiciona 'ndo'
# Se já termina em 'ndo', adiciona 'zinho'
def gerundio(s):
    return


# H. muito_bom
# Procura 'muito' e 'bom' na string
# Se 'bom' aparece depois de 'muito', troca por 'ótimo'
def muito_bom(s):
    return


# I. meio_meio
# Divide string em dois pedaços iguais
# Se ímpar, primeiro tem um a mais
# Dadas 2 strings a, b, retorna: meio1_a + meio1_b + meio2_a + meio2_b
def meio_meio(a, b):
    return


# J. noves_finais
# Conta quantos 9s há no final de um número
# noves_finais(1999) -> 2
def noves_finais(n):
    return


# K. conta5
# Conta quantas vezes o dígito 5 aparece entre 0 e n-1
def conta5(n):
    return


# L. potencia_de_3_com_inicio
# Retorna primeira potência de 3 que começa com n
def potencia3_inicio(n):
    return

def main():
    
    print('Gerundio')
    test(gerundio('correr'), 'correrndo')
    test(gerundio('correndo'), 'correndozinho')
    test(gerundio('eu'), 'eu')
    
    print()
    print('Muito_bom')
    test(muito_bom('Este filme é muito bom'), 'Este filme é ótimo')
    test(muito_bom('muito bom!'), 'ótimo!')
    
    print()
    print('Meio_meio')
    test(meio_meio('abcd', 'xy'), 'abxcdy')
    test(meio_meio('abcde', 'xyz'), 'abcxydez')
    
    print()
    print('Noves_finais')
    test(noves_finais(1999), 2)
    test(noves_finais(9999), 4)
    test(noves_finais(123), 0)
    
    print()
    print('Conta5')
    test(conta5(50), 15)
    test(conta5(100), 20)
    
    print()
    print('Potencia3_inicio')
    test(potencia3_inicio(27), 3)
    test(potencia3_inicio(81), 4)

if __name__ == '__main__':
    main()