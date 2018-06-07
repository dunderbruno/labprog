u"""Calcula tempo para ordenar lista com 10⁵ ítens."""

import time
import random


def insertionsort(lista):
    """Insertion Sort."""
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j-1
        while i >= 0 and lista[i] < chave:
            lista[i+1] = lista[i]
            i -= 1
        lista[i+1] = chave

begin = time.time()
a = [random.randint(1, 100000) for i in range(100000)]
finish = time.time()
print(finish-begin)
print(len(a))

# begin = time.time()
# insertionsort(a)
# finish = time.time()
# print(finish-begin)
