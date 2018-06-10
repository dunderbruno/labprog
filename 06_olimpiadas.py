# -*- coding: utf-8 -*-

u"""
Olimpíadas.

Ordena o quadro de medalhas.

Aluno: Bruno Olimpio dos Santos.
e-mail: belbrunosantos@gmail.com
"""


class pais:
    u"""Classe país."""

    def __init__(self, id):
        """Construtor."""
        self.id = id
        self.ouro = 0
        self.prata = 0
        self.bronze = 0

    def add_ouro(self):
        """Acrescenta medalha de ouro."""
        self.ouro += 1

    def add_prata(self):
        """Acrescenta medalha de prata."""
        self.prata += 1

    def add_bronze(self):
        """Acrescenta medalha de bronze."""
        self.bronze += 1


def ouro(lista):
    """Ordena pelas medalhas de ouro."""
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j-1
        while i >= 0 and lista[i].ouro < chave.ouro:
            lista[i+1] = lista[i]
            i -= 1
        lista[i+1] = chave


def prata(lista):
    """Desempata pelas medalhas de prata."""
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j-1
        if lista[i].ouro == chave.ouro:
            while i >= 0 and lista[i].prata < chave.prata:
                lista[i+1] = lista[i]
                i -= 1
            lista[i+1] = chave


def bronze(lista):
    """Desempata pelas medalhas de bronze."""
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j-1
        if (lista[i].ouro == chave.ouro):
            if (lista[i].prata == chave.prata):
                while i >= 0 and lista[i].bronze < chave.bronze:
                    lista[i+1] = lista[i]
                    i -= 1
                lista[i+1] = chave


def id(lista):
    """Desempata pelo menor id."""
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j-1
        if ((lista[i].ouro == chave.ouro) and
            (lista[i].prata == chave.prata) and
            (lista[i].bronze == chave.bronze)):
            while i>=0 and lista[i].id>chave.id:
                lista[i+1] = lista[i]
                i -= 1
            lista[i+1] = chave


N, M = input().split(' ')  # Paises e modalidades
N = int(N)
M = int(M)

paises = [pais(i) for i in range(1, N+1)]

for i in range(M):
    O, P, B = tuple(input().split(' '))
    O, P, B = int(O), int(P), int(B)
    paises[O-1].add_ouro()
    paises[P-1].add_prata()
    paises[B-1].add_bronze()

ouro(paises)
prata(paises)
bronze(paises)
id(paises)

saida = ''
for i in paises:
    saida += str(i.id)
    saida += ' '
print(saida[:-1])
