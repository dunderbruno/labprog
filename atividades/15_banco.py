u"""
Juvenal Vai ao Banco Brigar.

Aluno: Bruno Olimpio dos Santos
"""


class node:
    u"""Unidade básica da lista encadeada."""

    def __init__(self, dado):
        """Inicializa apenas com atributo [dado]."""
        self.dado = dado
        self.next = None

    def getDado(self):
        """Retorna o valor de self.dado."""
        return self.dado

    def getNext(self):
        """Retorna o valor de self.next."""
        return self.next

    def setDado(self, dado):
        """Altera o valor de self.dado."""
        self.dado = dado

    def setNext(self, next):
        u"""Altera ponteiro para o nó seguinte."""
        self.next = next


class Lista:
    """Classe Lista Encadeada."""

    def __init__(self):
        """Construtor da Lista."""
        self.primeiro = None
        self.ultimo = None

    def insertAtEnd(self, value):
        u"""Insere elemento no início da lista."""
        newNode = node(value)

        if self.isEmpty():
            self.primeiro = self.ultimo = newNode
        else:
            self.ultimo.setNext(newNode)
            self.ultimo = newNode

    def removeFromBegin(self):
        """Remove primeiro elemento."""
        firstNodeValue = self.primeiro.getDado()
        if self.primeiro is self.ultimo:
            self.primeiro = self.ultimo = None
        else:
            self.primeiro = self.primeiro.getNext()
        return firstNodeValue

    def isEmpty(self):
        u"""Retorna True se a lista está vazia."""
        return self.primeiro is None


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
            # print('%s %s' % (str(a), str(b)))
            saidas.append('%s %s' % (str(a), str(b)))
            # print(A.primeiro.getDado(), ' ', B.primeiro.getDado())

for i in saidas:
    print(i)
