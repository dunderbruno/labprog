u"""
Binary Search Tree.

Baseado em Introduction to Algorithms, Third Edition

Bruno Olimpio dos Santos
"""


class Node():
    u"""Unidade básica para funcionamento da Árvore Binária."""

    def __init__(self, key, data):
        u"""Classe Node é iniciada com argumentos key e data.

        Argumentos:
            key  - identificador de um objeto Node. Tipo - Inteiro.
            data - informação armazenada pelo objeto Node.

        Atributos:
            left   - filho esquerdo
            right  - filho direito
            parent - nó pai
        """
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def getKey(self):
        """Retorna chave de acesso."""
        return self.key

    def getData(self):
        u"""Retorna conteúdo armazenado."""
        return self.data

    def getLeft(self):
        """Retorna filho esquerdo."""
        return self.left

    def getRight(self):
        """Retorna filho direito."""
        return self.right

    def getParent(self):
        u"""Retorna nó pai."""
        return self.parent

    def setKey(self, key):
        """Define chave de acesso."""
        self.key = key

    def setData(self, data):
        u"""Define conteúdo armazenado."""
        self.data = data

    def setLeft(self, left):
        """Define filho esquerdo."""
        self.left = left

    def setRight(self, right):
        """Define filho direito."""
        self.right = right

    def setParent(self, parent):
        u"""Define nó pai."""
        self.parent = parent


class Tree():
    u"""Árvore de Busca Binária."""

    def __init__(self, root):
        u"""
        Inicia a Árvore com um objeto Node como raiz.

        t = Tree(Node(1,"a"))
        """
        self.root = root
