# -*- coding: utf-8 -*-

u"""
Juvenal Não Tem o Que Fazer.

Aluno: Bruno Olimpio dos Santos.
"""


def recursiva(n):
    """Faz chamadas recursivas e registra a quantidade."""
    global rodadas
    if n == 1:
        rodadas += 1
    elif (n % 2) == 0:
        rodadas += 1
        recursiva(n/2)
    elif (n % 2) == 1:
        rodadas += 1
        recursiva(3*n+1)
    return rodadas


T = int(input())
casos = []
for i in range(T):
    casos.append(input().split(' '))

rodadas = 0
for x in range(T):
    maior = 0
    for y in range(int(casos[x][0]), int(casos[x][1])):
        atual = recursiva(y)
        if atual > maior:
            maior = atual
        rodadas = 0
    print('Caso %d: %d' % (x+1, maior))
