# -*- coding: utf-8 -*-

u"""
Descobre a menor soma de fatoriais que formam um número.

Aluno: Bruno Olimpio dos Santos.
"""


def fatorial(n):
    u"""Calcula fatorial de um número."""
    return 1 if n < 2 else n*fatorial(n-1)


def maior(entrada):
    """Define o primeiro fatorial menor que o valor de entrada."""
    primeiro = 1
    while fatorial(primeiro) < entrada:
        primeiro += 1

    if fatorial(primeiro) > entrada:
        primeiro = primeiro - 1

    if (entrada - fatorial(primeiro)) > 0:
        maior(primeiro)

    return(primeiro)


entrada = int(input())
fatoriais = 0

while entrada > 0:
    entrada = entrada - fatorial(maior(entrada))
    fatoriais += 1

print(fatoriais)
