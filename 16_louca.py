u"""
Juvenal não quer lavar louça.

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

    def __init__(self, Id):
        """Construtor da Lista."""
        self.Id = Id
        self.primeiro = None
        self.ultimo = None
        self.atual = None

    def isEmpty(self):
        u"""Verifica se a lista está vazia."""
        return self.primeiro is None

    def __str__(self):
        u"""Representação em string."""
        if self.isEmpty():
            return ""
        atual = self.primeiro
        string = ""
        while atual is not None:
            string += str(atual.getDado()) + " "
            atual = atual.getNext()
            if atual == self.ultimo:
                break
        return string

    def insertAtEnd(self, value):
        u"""Insere elemento no início da lista."""
        newNode = node(value)

        if self.isEmpty():
            self.primeiro = self.ultimo = self.atual = newNode
        else:
            self.ultimo.setNext(newNode)
            self.ultimo = newNode
            self.ultimo.setNext(self.primeiro)

    def remove(self, alvo):  # SAIR DA FILA
        u"""Retirar um nó do meio."""
        if self.isEmpty():
            return ""
        atual = self.primeiro
        while atual.getNext() is not None:
            if atual.getNext().getDado() == alvo:
                proximo = atual.getNext().getNext()
                atual.setNext(proximo)
            atual = atual.getNext()

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

    def setAtual(self, atual):
        """Define Atual."""
        self.atual = atual

    def getAtual(self):
        """Retorna self.atual."""
        return self.atual.getDado()

    def s2l(self, string):
        """Transforma uma string em Lista Encadeada."""
        for i in string.split(' '):
            self.insertAtEnd(i)
            # return lista


F = int(input('F: '))  # quantas festas Juvenal realizou
deck = input('Deck: ')  # configuração inicial do deck
DECK = Lista(None)
DECK.s2l(deck)
vencedores = []
festas = []

for i in range(F):
    festas.append([])
contador_festas = 0
contador_baralhos = 1
while True:
    baralho = input('baralho: ')
    if baralho == '-1':
        contador_festas += 1
        contador_baralhos = 1
        if contador_festas == F:
            break
    else:
        BARALHO = Lista(contador_baralhos)
        BARALHO.s2l(baralho)
        festas[contador_festas].append(BARALHO)
        contador_baralhos += 1

# for i in festas:
#     for j in i:
#         print(j.primeiro.getDado())

festa = 0
rodadas = 0
while rodadas <= 1000:
    if len(vencedores) == F:
        break
    elif rodadas == 1000:
        vencedores.append(0)
        break
    # print('passei aqui')
    rodadas += 1
    Atual = DECK.getAtual()
    for i in festas[festa]:
        if i.isEmpty():
            vencedores.append(i.Id)
            break
        elif i.getAtual() == Atual:
            print('carta ', i.getAtual(), 'de', i.Id, '==', Atual)
            i.setAtual(i.atual.getNext())
            if i.primeiro.getDado() == Atual:
                i.removeFromBegin()
            elif i.ultimo.getDado() == Atual:
                i.removeFromEnd()
            else:
                i.remove(Atual)
        else:
            print('carta ', i.getAtual(), '!=', Atual)
            i.setAtual(i.atual.getNext())
    DECK.setAtual(DECK.atual.getNext())

print(rodadas)
print(vencedores)