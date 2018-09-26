# -*- coding: utf-8 -*-

u"""
Quebrando a banca.

Recebe um número e a quantidade de digitos a ser retirada.
Retorna o maior inteiro possível.

Aluno: Bruno Olimpio dos Santos.
"""


def varredura(inicio, fim, lista):
    """Varre a lista em busca do maior valor."""
    maior = 0
    for i in range(B+1):
        if len(lista[inicio:fim]) >= 1 and int(lista[inicio:fim]) > maior:
            maior = int(lista[inicio:fim])
            indice = int(inicio)
        inicio += 1
        fim += 1
    return(indice)


RESULTADOS = []

while True:
    try:
        A, B = input("A, B: ").split(' ')
        A = int(A)
        B = int(B)
        saldo = input('Saldo: ')

        si = 0  # inicio do slice
        sf = A - B  # fim do slice
        rodadas = A - B
        resultado = ''

        for i in range(rodadas):
            resultado += (saldo[varredura(si, sf, saldo)])
            si = varredura(si, sf, saldo) + 1
            sf = sf + 1

        RESULTADOS.append(resultado)

    except:
            break

for r in RESULTADOS:
    print(r)
