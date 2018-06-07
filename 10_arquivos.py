# -*- coding: utf-8 -*-

u"""
Arquivos.

Quantidade mínima possível de pastas
de tamanho B para armazenar N arquivos

Aluno: Bruno Olimpio dos Santos.
e-mail: belbrunosantos@gmail.com
"""


def pasta(lista, tamanho_maximo):
    """Varre a lista e forma uma pasta."""
    soma = 0
    numeros = []
    for i in range(len(lista)):
        if i > 0:
            if soma + lista[i] <= B and len(numeros) < 2:
                soma = soma + lista[i]
                lista[i] = 0
    print(numeros)
    print(soma)


N, B = input().split(' ')
N = int(N)
B = int(B)
arquivos = input().split(' ')
arquivos = [int(i) for i in arquivos]
arquivos.sort(reverse=True)
print(arquivos)
pasta(arquivos, B)
print(arquivos)
pasta(arquivos, B)
print(arquivos)
pasta(arquivos, B)
print(arquivos)
