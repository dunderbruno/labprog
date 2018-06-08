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

while True:
    if arquivos[0] == B:
        print('pasta', arquivos[0])
        arquivos.pop(0)
    else:
        break


while len(arquivos) > 1:
    for i in range(len(arquivos)):
        if arquivos[0]+arquivos[i] == B:
            print('pasta ', arquivos[0], arquivos[i])
            arquivos.pop(i)
            arquivos.pop(0)
        if len(arquivos) <= 1:
            break
