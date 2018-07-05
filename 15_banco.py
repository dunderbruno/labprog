u"""
Juvenal Vai ao Banco Brigar.

Aluno: Bruno Olimpio dos Santos
"""

from lista_encadeada import node
from lista_encadeada import Lista


saidas = []

T = int(input('T: '))  # casos de teste
for t in range(T):
    saidas.append('Caso %s:' % str(t+1))
    A = Lista()  # fila regular
    B = Lista()  # fila preferencial
    N = int(input('N: '))  # quantidade de comandos em cada caso
    for n in range(N):
        comando = input('~$ ')
        if comando[0] == 'f':
            A.insertAtEnd(comando.split(' ')[1])
        elif comando[0] == 'p':
            B.insertAtEnd(comando.split(' ')[1])
        elif comando == 'A':
            if A.isEmpty():
                if B.isEmpty():
                    pass
                B.removeFromBegin()
            else:
                A.removeFromBegin()
        elif comando == 'B':
            if B.isEmpty():
                if A.isEmpty():
                    pass
                A.removeFromBegin()
            else:
                B.removeFromBegin()
        elif comando == 'I':
            if A.isEmpty():
                a = '0'
            else:
                a = A.primeiro.getDado()
            if B.isEmpty():
                b = '0'
            else:
                b = B.primeiro.getDado()
            print('%s %s' % (str(a), str(b)))
            # saidas.append('%s %s' % (str(a), str(b)))
            # print(A.primeiro.getDado(), ' ', B.primeiro.getDado())

for i in saidas:
    print(i)
# 3
# 6
# f 3
# I
# p 5
# p 7
# A
# I
