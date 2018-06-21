"""
Ortografia.

Aluno: Bruno Olimpio dos Santos.
e-mail: belbrunosantos@gmail.com
"""


def minimo(sequencia):
    u"""Recebe uma sequência e retorna valor mínimo."""
    menor = sequencia[0]
    for i in sequencia:
        if menor > i:
            menor = i
    return menor


def distancia(A, B):
    u"""Distância de Edição."""
    m = len(A)
    n = len(B)
    M = []

    for x in range(m+1):
        M.append([])
        for y in range(n+1):
            M[x].append((0))

    for i in range(0, m+1):
        M[i][0] = i

    for j in range(0, n+1):
        M[0][j] = j

    for x in range(1, m+1):
        for y in range(1, n+1):
            if A[x-1] == B[y-1]:
                cost = 0
            else:
                cost = 1

            M[x][y] = minimo((M[x-1][y-1] + cost,
                              M[x-1][y] + 1,
                              M[x][y-1] + 1,))

    return(M[m][n])


def refere(palavra):
    """Retorna palavras do dicionario com distância de edição <= 2."""
    saida = ''
    for i in dicionario:
        if distancia(palavra, i) <= 2:
            saida = saida + i + ' '
    return(saida)


N, M = input().split(' ')
N, M = int(N), int(M)

dicionario = [input() for i in range(N)]
formulario = [input() for i in range(M)]

for i in formulario:
    print(refere(i)[:-1])
