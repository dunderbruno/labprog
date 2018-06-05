def maximo(lista):
    maximo = lista[0]
    for i in lista:
        if maximo < i:
            maximo = i
    return maximo

def recursiva(n):
    global rodadas
    if n == 1:
        # print('1')
        rodadas+=1
    elif (n % 2) == 0:
        # print('par')
        rodadas+=1
        recursiva(n/2)
    elif (n % 2) == 1:
        # print('impar')
        rodadas+=1
        recursiva(3*n+1)

resultados=[]

rodadas = 0
for i in range(900,1000):

    # n=int(input())
    n=i
    recursiva(n)
    # print('variavel rodadas: ',rodadas)
    resultados.append(rodadas)
    rodadas=0


# print(resultados)
# print(len(resultados))
print(maximo(resultados))
