u"""
Juvenal Vai ao Banco Brigar.

Aluno: Bruno Olimpio dos Santos
"""

from lista_encadeada import node
from lista_encadeada import Lista

T = int(input('T: '))  # casos de teste
for t in range(T):
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
            A.removeFromBegin()
        elif comando == 'B':
            B.removeFromBegin()
        elif comando == 'I':
            print(A.primeiro.getDado(), ' ', B.primeiro.getDado())
