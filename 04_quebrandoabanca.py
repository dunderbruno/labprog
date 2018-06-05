# Aluno: Bruno Olimpio dos Santos
# e-mail: belbrunosantos@gmail.com

def maximo(saldo):
    maior  = saldo[0]
    indice = 0
    for i in range(len(saldo)):
        if saldo[i] > maior:
            maior=saldo[i]
            indice=i
        elif saldo[i] < maior:
            continue
    maiores.append(saldo.pop(indice))
    indices.append(indice)

def bubblesort(z):
    for i in range(len(z)-1):
        if z[i]>z[i+1]:
            z[i],z[i+1]=z[i+1],z[i]
            for i in range(len(z)-1):
                if z[i]>z[i+1]:
                    z[i],z[i+1]=z[i+1],z[i]
                    for i in range(len(z)-1):
                        if z[i]>z[i+1]:
                            z[i],z[i+1]=z[i+1],z[i]

RESULTADOS = []

while True:
    try:
        AB = input("A, B: ")
        A,B = AB.split(' ')
        saldo = list(input('Saldo: '))
        deixar = int(A) - int(B)
        permuta = [(saldo[i:j]) for i in range(len(saldo)+1)
                                   for j in range(len(saldo)+1)
                                   if len(saldo[i:j])==deixar]
        bubblesort(permuta)
        possivel = ''
        for p in permuta[-1]:
            possivel+=p
        possivel=int(possivel)

        if saldo == saldo[::-1]:
            saida = ''
            for s in range(int(A)-int(B)):
                saida = saida + saldo[s]
            saida = int(saida)
            if possivel > saida:
                saida = possivel
            RESULTADOS.append(saida)

        elif AB == 'endOfFile':
            break

        else:
            saldo_backup = saldo[:]
            maiores, indices, resultado = [],[],[]
            saida = ''

            for i in range(int(A) - int(B)):
                maximo(saldo)

            for i in range(len(maiores)):
                for j in range(len(saldo_backup)):
                    if maiores[i] == saldo_backup[j]:
                        resultado.append(j)
            bubblesort(resultado)

            for r in resultado:
                saida = saida + str(saldo_backup[r])
            saida = int(saida)
            if possivel > saida:
                saida = possivel
            # print(saida)
            RESULTADOS.append(saida)
    except:
            break

for resultado in RESULTADOS:
    print(resultado)
