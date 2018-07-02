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

class encadeada:
    """Lista Encadeada."""

    def __init__(self):
        u"""Ponteiros para primeiro e ultimo nós."""
        self.first = None
        self.last = None

    def empty()
