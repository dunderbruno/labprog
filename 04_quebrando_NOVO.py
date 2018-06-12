"""quebrando a banca."""

A, B = input("A, B: ").split(' ')
A = int(A)
B = int(B)
saldo = input('Saldo: ')
# print(len(saldo))


si = 0  # inicio do slice
sf = A - B  # fim do slice
rodadas = A - B
resultado = ''


def varredura(inicio, fim, lista):
    """Varre a lista."""
    maior = 0
    for i in range(B+1):
        # print('maior', maior)
        # print(lista[inicio:fim])
        if len(lista[inicio:fim]) >= 1 and int(lista[inicio:fim]) > maior:
            maior = int(lista[inicio:fim])
            indice = int(inicio)
        inicio += 1
        fim += 1
    # print('rodei')
    return(indice)


# print(varredura(si, sf, saldo))
# print(saldo[varredura(si, sf, saldo)])

for i in range(rodadas):
    resultado += (saldo[varredura(si, sf, saldo)])
    si = varredura(si, sf, saldo) + 1
    sf = sf + 1

print(resultado)
# print(saldo[(varredura(inicio, fim, saldo))])
# print(saldo[partida+1:])
# print(varredura(2, fim, saldo))
# for i in range(fim):
#     atual = int((saldo[varredura(inicio, fim, saldo)]))
#     saldo = saldo[atual:]
