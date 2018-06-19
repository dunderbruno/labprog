"""
Ortografia.

Aluno: Bruno Olimpio dos Santos.
e-mail: belbrunosantos@gmail.com
"""

from labtools import levenshtein

N, M = input().split(' ')
N, M = int(N), int(M)

dicionario = [input() for i in range(N)]
formulario = [input() for i in range(M)]


def refere(palavra):
    """Retorna palavras do dicionario com Levenshtein <= 2."""
    saida = ''
    for i in dicionario:
        if levenshtein(palavra, i) <= 2:
            saida = saida + i + ' '
    return(saida)


for i in formulario:
    print(refere(i)[:-1])
