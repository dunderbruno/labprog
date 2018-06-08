# -*- coding: utf-8 -*-

u"""
Arquivos.

Quantidade mínima possível de pastas
de tamanho B para armazenar N arquivos

Aluno: Bruno Olimpio dos Santos.
e-mail: belbrunosantos@gmail.com
"""


N, B = input().split(' ')
N, B = int(N), int(B)
arquivos = input().split(' ')
arquivos = [int(i) for i in arquivos]
arquivos.sort(reverse=True)

pastas = 0


for i in range(len(arquivos)):
    if arquivos[i] == B:
        ultimo = i
        # print('pasta', i)
        pastas += 1
    else:
        break
for i in range(ultimo, -1, -1):
    arquivos.pop(i)

print(arquivos)
print(pastas)
