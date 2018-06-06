# -*- coding: utf-8 -*-

u"""
Arquivos.

Aluno: Bruno Olimpio dos Santos.
e-mail: belbrunosantos@gmail.com
"""


def InsertionSort(lista):
    u"""Ordenação."""
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j-1
        while i >= 0 and lista[i] > chave:
            lista[i+1] = lista[i]
            i -= 1
        lista[i+1] = chave


N, B = input().split(' ')
N = int(N)
B = int(B)
arquivos = input().split(' ')
arquivos = [int(i) for i in arquivos]
# a=[int(input()) for i in range(3)]
# 5 4
# 4 3 1 2 2
