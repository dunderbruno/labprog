def maximo(lista):
    maximo = lista[0]
    for i in lista:
        if maximo < i:
            maximo = i
    return maximo

def fatias(tamanhos,menor):
    fatias = 0
    for i in tamanhos:
        fatias = fatias + (i//menor)
    return fatias

N = int(input())
K = int(input())
tamanhos = input().split(' ')
tamanhos = [int(i) for i in tamanhos]
# for t in range(len(tamanhos)):
#     tamanhos[t] = int(tamanhos[t])

for i in range(1,maximo(tamanhos)):
    if fatias(tamanhos,i) == N:
        maior = i

print(maior)