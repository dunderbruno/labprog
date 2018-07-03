"""Lista Encadeada."""


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

    def __str__(self):
        u"""Representação em string."""
        if self.isEmpty():
            return ""
        atual = self.primeiro
        string = ""
        while atual is not None:
            string += str(atual.getDado()) + " "
            atual = atual.getNext()
        return string

    def sair(self, alvo):  # SAIR DA FILA
        u"""Retirar um nó do meio."""
        if self.isEmpty():
            return ""
        atual = self.primeiro
        while atual.getNext() is not None:
            if atual.getNext().getDado() == alvo:
                proximo = atual.getNext().getNext()
                atual.setNext(proximo)
            atual = atual.getNext()

    def insertAtBegin(self, value):
        u"""Adiciona nó na primeira posição."""
        newNode = node(value)  # instancia de um novo nodo
        if self.isEmpty():  # Insersao para Lista vazia
            self.primeiro = self.ultimo = newNode
        else:                   # Insersao para lista nao vazia
            newNode.setNext(self.primeiro)
            self.primeiro = newNode

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

    def removeFromEnd(self):
        """Remove o ultimo elemento."""
        lastNodeValue = self.ultimo.getDado()
        if self.primeiro is self.ultimo:
            self.primeiro = self.ultimo = None
        else:
            atual = self.primeiro
            while atual.getNext() is not self.ultimo:
                atual = atual.getNext()
            atual.setNext(None)
            self.ultimo = atual
        return lastNodeValue

    def isEmpty(self):
        return self.primeiro is None


# class encadeada:
#     """Lista Encadeada."""
#
#     def __init__(self):
#         u"""Ponteiros para primeiro e ultimo nós."""
#         self.first = None
#         self.last = None
#
#     def empty()
