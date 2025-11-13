print('\n\n=== LISTA 2 - STRINGS ===\n')

def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))
    

# A. rosquinhas
# Para um inteiro n retorna 'Número de rosquinhas: <n>'
# Caso n >= 12 retorna 'muitas'
# rosquinhas(5) -> 'Número de rosquinhas: 5'
# rosquinhas(15) -> 'Número de rosquinhas: muitas'
def rosquinhas(n):
    return


# B. extremos
# Dada uma string s, retorna as três primeiras e três últimas letras
# Assim 'programacao' retorna 'proção'
# Se tiver menos que 3 letras, retorna string vazia
def extremos(s):
    return


# C. marca_primeiro
# Dada uma string s, troca todas as ocorrências
# do primeiro caractere por '#', exceto o primeiro
# Assim 'elefante' retorna 'el#fant#'
def marca_primeiro(s):
    return


# D. troca3
# Sejam duas strings a e b
# Retorna '<a> <b>' com as três primeiras letras trocadas
# 'hello', 'world' -> 'worlo helld'
def troca3(a, b):
    return


# E. anagrama
# Verifica se duas strings são anagramas
# (mesmas letras em ordem diferente)
# anagrama('amor', 'roma') -> True
# anagrama('casa', 'saca') -> True
def anagrama(a, b):
    return


# F. conta_palavra
# Conta ocorrências de uma palavra em uma frase
# conta_palavra('o rato roeu a roupa do rei', 'ro') -> 3
def conta_palavra(frase, palavra):
    return

def main():
    print('Rosquinhas')
    test(rosquinhas(5), 'Número de rosquinhas: 5')
    test(rosquinhas(12), 'Número de rosquinhas: muitas')
    test(rosquinhas(15), 'Número de rosquinhas: muitas')
    
    print()
    print('Extremos')
    test(extremos('programacao'), 'proção')
    test(extremos('python'), 'python')
    test(extremos('ab'), '')
    
    print()
    print('Marca_primeiro')
    test(marca_primeiro('elefante'), 'el#fant#')
    test(marca_primeiro('banana'), 'b#n#n#')
    
    print()
    print('Troca3')
    test(troca3('hello', 'world'), 'worlo helld')
    test(troca3('abc', 'xyz'), 'xyzabc ')
    
    print()
    print('Anagrama')
    test(anagrama('amor', 'roma'), True)
    test(anagrama('casa', 'saca'), True)
    test(anagrama('teste', 'outro'), False)
    
    print()
    print('Conta_palavra')
    test(conta_palavra('o rato roeu a roupa do rei', 'ro'), 3)
    test(conta_palavra('banana', 'na'), 2)

if __name__ == '__main__':
    main()