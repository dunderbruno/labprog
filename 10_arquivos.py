# -*- coding: utf-8 -*-

u"""
Arquivos.

Quantidade mínima possível de pastas
de tamanho B para armazenar N arquivos

Aluno: Bruno Olimpio dos Santos.
e-mail: belbrunosantos@gmail.com
"""


def reverse(lista):
    """Insertion Sort - REVERSE."""
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j-1
        while i >= 0 and lista[i] < chave:
            lista[i+1] = lista[i]
            i -= 1
        lista[i+1] = chave


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
# arquivos.sort(reverse=True)
reverse(arquivos)
pastas = 0

print('Contando arquivos de tamanho = B')
for i in range(len(arquivos)):
    if arquivos[i] == B:
        ultimo = i
        pastas += 1
    else:
        break
for i in range(ultimo, -1, -1):
    arquivos.pop(i)
print(pastas)

print('Contando duplas x+y=B')
for i in range((N//2) + 1):
    if dupla(arquivos):
        pastas += 1
print(pastas)

print('Contando duplas x+y<B')
for i in range(len(arquivos)):
    if cabe(arquivos):
        pastas += 1
print(pastas)

print('Contando sobras')
pastas += len(arquivos)
print(pastas)
