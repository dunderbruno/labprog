# -*- coding: utf-8 -*-

u"""
Arquivos.

Quantidade mínima possível de pastas
de tamanho B para armazenar N arquivos

Aluno: Bruno Olimpio dos Santos.
e-mail: belbrunosantos@gmail.com
"""


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, (r-1)+1):
        if A[j] > x:  # DECRESCENTE
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


def dupla(lista):
    """Encontra dois numeros que somam B."""
    for i in range(len(lista)):
        if lista[0]+lista[i] == B:
            lista.pop(i)
            lista.pop(0)
            return True


def cabe(lista):
    """Forma pastas com soma menor que B."""
    if len(lista) > 1:
        for i in range(len(lista)):
            if lista[0] + lista[i] < B:
                lista.pop(i)
                lista.pop(0)
                return True


N, B = input().split(' ')
N, B = int(N), int(B)
arquivos = input().split(' ')
arquivos = [int(i) for i in arquivos]
quicksort(arquivos, 0, len(arquivos)-1)  # DECRESCENTE
pastas = 0
ultimo = 0
# Contando arquivos de tamanho = B
for i in range(len(arquivos)):
    if arquivos[i] == B:
        ultimo = i
        pastas += 1
    else:
        break
for i in range(ultimo, -1, -1):
    arquivos.pop(i)

# Contando duplas x + y = B
for i in range((N//2) + 1):
    if dupla(arquivos):
        pastas += 1

# Contando duplas x + y < B
for i in range(len(arquivos)):
    if cabe(arquivos):
        pastas += 1

# Contando excedentes
pastas += len(arquivos)

print(pastas)
