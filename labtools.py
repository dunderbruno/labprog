u"""Biblioteca de funções para Laboratório de Programação."""


def maximo(sequencia):
    u"""Recebe uma sequência e retorna o valor máximo."""
    maior = sequencia[0]
    for i in sequencia:
        if maior < i:
            maior = i
    return maior


def minimo(sequencia):
    u"""Recebe uma sequência e retorna o valor mínimo."""
    menor = sequencia[0]
    for i in sequencia:
        if menor > i:
            menor = i
    return menor


def fatorial(n):
    u"""Calcula fatorial de um número."""
    return 1 if n < 2 else n*fatorial(n-1)


def insertionsort(lista):
    """Recebe um conjunto e ordena com Insertion Sort."""
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j-1
        while i >= 0 and lista[i] > chave:
            lista[i+1] = lista[i]
            i -= 1
        lista[i+1] = chave


def reverse(lista):
    """Recebe um conjunto e ordena com Insertion Sort - DECRESCENTE."""
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j-1
        while i >= 0 and lista[i] < chave:
            lista[i+1] = lista[i]
            i -= 1
        lista[i+1] = chave


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, (r-1)+1):
        if A[j] < x:  # para ordem decrescente inverter operador < para >
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


def levenshtein(A, B):
    """Levenshtein Distance."""
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
