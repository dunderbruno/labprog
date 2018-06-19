from labtools import levenshtein

N, M = input().split(' ')
N, M = int(N), int(M)

dicionario = [input() for i in range(N)]
formulario = [input() for i in range(M)]
