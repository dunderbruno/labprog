# -*- coding: utf-8 -*-

u"""
Arquivos.

Quantidade mínima possível de pastas
de tamanho B para armazenar N arquivos

Aluno: Bruno Olimpio dos Santos.
e-mail: belbrunosantos@gmail.com
"""


def dupla(lista):
    """Encontra dois numeros que somam B."""
    for i in range(len(lista)):
        if lista[0]+lista[i] == B:
            lista.pop(i)
            lista.pop(0)
            return True


N, B = input().split(' ')
N, B = int(N), int(B)
arquivos = input().split(' ')
arquivos = [int(i) for i in arquivos]
arquivos.sort(reverse=True)

pastas = 0

for i in range(len(arquivos)):
    if arquivos[i] == B:
        ultimo = i
        pastas += 1
    else:
        break
for i in range(ultimo, -1, -1):
    arquivos.pop(i)

print(pastas)

for i in range((N//2) + 1):
    if dupla(arquivos):
        pastas += 1

print(pastas)
# print(dupla(arquivos))
# print(dupla(arquivos))
# print(dupla(arquivos))

# print(pastas)
print(arquivos)
# for i in arquivos:
#     print('pasta', i)
