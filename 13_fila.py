# -*- coding: utf-8 -*-

u"""
Ninguém aguenta mais filas.

Aluno: Bruno Olimpio dos Santos.
e-mail: belbrunosantos@gmail.com
"""


class Nodo:
    u"""Classe Nó"""

    def __init__(self, conteudo):
        """Construtor."""
        self.conteudo = conteudo
        self.seguinte = None

    def getData(self):
        u"""Retorna conteúdo do nó."""
        return self.conteudo

    def setData(self, conteudo):
        u"""Define valor do nó."""
        self.conteudo = conteudo

    def getNextNode(self):
        u"""Retorna o proximo nó."""
        return self.seguinte

    def setNextNode(self, newNode):
        u"""Define o próximo nó."""
        self.seguinte = newNode


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
            string += str(atual.getData()) + " "
            atual = atual.getNextNode()
        return string

    def sair(self, alvo):  # SAIR DA FILA
        u"""Retirar um nó do meio."""
        if self.isEmpty():
            return ""
        atual = self.primeiro
        while atual.getNextNode() is not None:
            if atual.getNextNode().getData() == alvo:
                proximo = atual.getNextNode().getNextNode()
                atual.setNextNode(proximo)
            atual = atual.getNextNode()

    def insertAtBegin(self, value):
        u"""Adiciona nó na primeira posição."""
        newNode = Nodo(value)  # instancia de um novo nodo
        if self.isEmpty():  # Insersao para Lista vazia
            self.primeiro = self.ultimo = newNode
        else:                   # Insersao para lista nao vazia
            newNode.setNextNode(self.primeiro)
            self.primeiro = newNode

    def insertAtEnd(self, value):
        u"""Insere elemento no início da lista."""
        newNode = Nodo(value)

        if self.isEmpty():
            self.primeiro = self.ultimo = newNode
        else:
            self.ultimo.setNextNode(newNode)
            self.ultimo = newNode

    def removeFromBegin(self):
        """Remove primeiro elemento."""
        firstNodeValue = self.primeiro.getData()
        if self.primeiro is self.ultimo:
            self.primeiro = self.ultimo = None
        else:
            self.primeiro = self.primeiro.getNextNode()
        return firstNodeValue

    def removeFromEnd(self):
        """Remove o ultimo elemento."""
        lastNodeValue = self.ultimo.getData()
        if self.primeiro is self.ultimo:
            self.primeiro = self.ultimo = None
        else:
            atual = self.primeiro
            while atual.getNextNode() is not self.ultimo:
                atual = atual.getNextNode()
            atual.setNextNode(None)
            self.ultimo = atual
        return lastNodeValue

    def isEmpty(self):
        return self.primeiro is None


N = int(input())
entraram = input().split(' ')
M = int(input())
sairam = input().split(' ')
fila = Lista()

for i in entraram:
    fila.insertAtEnd(i)

# print(fila)

for j in sairam:
    if fila.primeiro.getData() == j:
        fila.removeFromBegin()
    elif fila.ultimo.getData() == j:
        fila.removeFromEnd()
    else:
        fila.sair(j)

print(fila)
