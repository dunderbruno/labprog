u"""
Notação Polonesa.

Aluno: Bruno Olimpio dos Santos
"""


class Node:
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

    def insertAtBegin(self, value):
        u"""Adiciona nó na primeira posição."""
        newNode = Node(value)  # instancia de um novo nodo
        if self.isEmpty():  # Insersao para Lista vazia
            self.primeiro = self.ultimo = newNode
        else:                   # Insersao para lista nao vazia
            newNode.setNext(self.primeiro)
            self.primeiro = newNode

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


def processa(a, b, operador):
    u"""Decide qual operação retornar."""
    if operador == '+':
        return int(a) + int(b)
    elif operador == '-':
        return int(a) - int(b)
    elif operador == '*':
        return int(a) * int(b)
    elif operador == '/':
        return int(a) / int(b)


