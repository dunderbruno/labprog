# Aluno: Bruno Olimpio dos Santos
# e-mail: belbrunosantos@gmail.com

def linhas(quadrado):
    totais_linhas = []
    for linha in quadrado:
        soma_linha=0
        for elemento in linha:
            soma_linha = soma_linha + int(elemento)
        totais_linhas.append(soma_linha)
        somas.append(soma_linha)

def colunas(quadrado,N):
    totais_colunas = []
    for i in range(N):
        soma_colunas = 0
        for j in range(N):
            soma_colunas = soma_colunas + int(quadrado[j][i])
        totais_colunas.append(soma_colunas)
        somas.append(soma_colunas)

def diagonal_p(quadrado,N):
    diagonal_principal=0
    for i in range(N):
        for j in range(N):
            if i == j:
                diagonal_principal = diagonal_principal + int(quadrado[i][j])
    somas.append(diagonal_principal)

def diagonal_s(quadrado,N):
    diagonal_secundaria=0
    for i in range(N):
        for j in range(N-1,-1,-1):
            if i+j==N-1:
                diagonal_secundaria = diagonal_secundaria + int(quadrado[i][j])
    somas.append(diagonal_secundaria)

N = int(input())
quadrado = []
for i in range(N):
    quadrado.append(input().split(' '))
somas = []
magico=True

linhas(quadrado)
colunas(quadrado,N)
diagonal_p(quadrado,N)
diagonal_s(quadrado,N)

for v in range(len(somas)-1):
    if somas[v]==somas[0]:
        pass
    else:
        magico=False

if magico:
    print(somas[0])
else:
    print('-1')
