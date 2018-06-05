# Aluno: Bruno Olimpio dos Santos
# e-mail: belbrunosantos@gmail.com

def fatorial(n):
    return 1 if n < 2 else n*fatorial(n-1)

def maior(entrada):
    primeiro = 1
    while fatorial(primeiro) < entrada:
        primeiro += 1

    if fatorial(primeiro) > entrada:
        primeiro = primeiro - 1

    if (entrada - fatorial(primeiro)) > 0:
        maior(primeiro)

    return(primeiro)

# entrada = int(input('N: '))
entrada = int(input())
fatoriais = 0

while entrada > 0:
    entrada = entrada - fatorial(maior(entrada))
    fatoriais+=1

print(fatoriais)

74293
