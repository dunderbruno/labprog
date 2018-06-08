# -*- coding: utf-8 -*-

u"""
Juvenal Não Tem o Que Fazer.

Aluno: Bruno Olimpio dos Santos.
e-mail: belbrunosantos@gmail.com
"""
import time


def maximo(lista):
    u"""Encontra o maior número em uma lista."""
    maximo = lista[0]
    for i in lista:
        if maximo < i:
            maximo = i
    return maximo


def recursiva(n):
    """Faz chamadas recursivas e registra a quantidade."""
    global rodadas
    if n == 1:
        # print('1')
        rodadas += 1
    elif (n % 2) == 0:
        # print('par')
        rodadas += 1
        recursiva(n/2)
    elif (n % 2) == 1:
        # print('impar')
        rodadas += 1
        recursiva(3*n+1)
    return rodadas


rodadas = 0
# print(recursiva(10))

T = int(input())
casos = []
for i in range(T):
    casos.append(input().split(' '))


for x in casos:
    maior = 0
    for y in range(int(x[0]), int(x[1])):
        atual = recursiva(y)
        if atual > maior:
            maior = atual
        rodadas = 0
    print(maior)
