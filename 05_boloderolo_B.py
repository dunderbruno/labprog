# -*- coding: utf-8 -*-

u"""
Bolo de Rolo.

Versão com Árvore Binária
"""

from labtools import maximo
from labtools import minimo
from binarytree import No
from binarytree import tree


def fatias(tamanhos, largura):
    """Em quantas fatias iguais um conjunto pode ser dividido."""
    fatias = 0
    for i in tamanhos:
        fatias = fatias + (i//largura)
    return fatias


N = int(input())
K = int(input())
bolos = input().split(' ')
bolos = [int(i) for i in bolos]

menor = minimo(bolos)
maior = maximo(bolos)

x = tree(None)
x.populate(1, maior)
atual = x.raiz
while True:
    if fatias(bolos, atual.getChave()) == N:
        print(atual.getChave())
        break
    elif fatias(bolos, atual.getChave()) > N:
        atual = atual.getDir()
    elif fatias(bolos, atual.getChave()) < N:
        atual = atual.getEsq()
