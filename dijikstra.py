"""Algoritmo de Dijikstra."""

import math


class vertice():
    u"""Classe Vértice."""

    def __init__(self, key):
        """Construtor."""
        self.key = key
        self.distancia = 0
        self.vizinhos = []
        self.arestas = {}  # [vertice:distancia]

    def addVizinho(vertice):
        """Adiciona um vizinho."""
        self.vizinhos.append(vertice)

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
        u"""Retorna True se a lista está vazia."""
        return self.primeiro is None


def dijikstra(grafo, origem, destino):
    """Dijikstra Algorithm."""
    Q = Lista()
    origem.distancia = 0
    # ou seria adicionar ele mesmo na lista de vizinhos, com distancia =0?
    for v in grafo:
        v.distancia = math.inf  # no dicionário
        Q.insert(v)
    while Q.isEmpty() is not False:
        v = Q.min(v.distancia)
        Q.remove(v)
        for u in v.vizinhos:  # para cada vizinho u de v faça:
            novo = v.distancia + v.arestas[u.key]
            if novo < u.distancia:
            # "u" é o vizinho de "v". Na primeira rodada é infinito
                u.distancia = novo
    return destino.distancia


a = vertice(1)
b = vertice(2)
c = vertice(3)
d = vertice(4)
e = vertice(5)

G = [a, b, c, d, e]

dijikstra(G, 2, 5)
