# -*- coding: utf-8 -*-

u"""
Arquivos.

Quantidade mínima possível de pastas
de tamanho B para armazenar N arquivos

Aluno: Bruno Olimpio dos Santos.
e-mail: belbrunosantos@gmail.com
"""


def pasta(lista, tamanho):
    """Busca um numero que forme a pasta com o primeiro."""
    base = lista[0]
    global pastas
    for i in range(1, len(lista)):
        if base + lista[i] <= tamanho:
            lista.pop(i)
            lista.pop(0)
            pastas += 1
    print(lista)


N, B = input().split(' ')
N = int(N)
B = int(B)
arquivos = input().split(' ')
arquivos = [int(i) for i in arquivos]
arquivos.sort(reverse=True)
pastas = 0
print(len(arquivos))
while len(arquivos) > 0:
    pasta(arquivos, B)

print(pastas)
# print(len(arquivos))
# print(pastas)

# soma = 0
# for i in range(N+1):
#     cabe = 0
#     if (soma + i <= B) and (cabe < 2):
#         soma += i
#         cabe += 1
#         arquivos[i] = 999
#     if cabe == 2:
#         break
#
# print(soma)
# print(arquivos)
