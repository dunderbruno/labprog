"""
Juvenal se perdeu.

Aluno: Bruno Olimpio dos Santos
"""

class Node():
    u"""Unidade básica para funcionamento da Árvore Binária."""

    def __init__(self, key):
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
        self.data = None
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

    def __repr__(self):
        return self.getData()


class Tree():
    u"""Árvore de Busca Binária."""

    def __init__(self):
        u"""
        Inicia a Árvore com um objeto Node como raiz.

        t = Tree(Node(1,"a"))
        """
        self.root = None

    def setRoot(self, root):
        self.root = root

    def minimum(self, x):
        if x is not None:
            while x.getLeft() is not None:
                x = x.getLeft()
            return x.getKey()

    def maximum(self, x):
        if x is not None:
            while x.getRight() is not None:
                x = x.getRight()
            return x.getData()

    def successor(self, x):
        if x is not None:
            if x.getRight() is not None:
                return self.minimum(x.getRight())
            else:
                father = x.getParent()
                while father is not None and x is father.getRight():
                    x = father
                    father = x.getParent()
                    return father

    def antecessor(self, x):
        if x.getLeft() is not None:
            return self.maximum(x.getLeft())
        y = x.getParent()
        while (y is not None) and (x == y.getLeft()):
            x = y
            y = y.getParent()
        return y

    def insert(self, z):
        u"""Insere um objeto Node na árvore."""
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.getKey() < x.getKey():
                x = x.getLeft()
            else:
                x = x.getRight()
        z.setParent(y)
        if y is None:
            self.root = z
        elif z.getKey() < y.getKey():
            y.setLeft(z)
        else:
            y.setRight(z)

    def delete(self, z):
        if (z.getLeft() is None) or (z.getRight() is None):
            y = z
        else:
            y = z.successor()
        if y.getLeft() is not None:
            x = y.getLeft()
        else:
            x = y.getRight()
        if x is not None:
            x.setParent(y.getParent())
        if y.getParent() is None:
            self.root = x
        else:
            if y == y.getParent().getLeft():
                y.getParent().setLeft(x)
            else:
                y.getParent().setRight(x)

        if y != z:
            z.setKey(y.getKey())
        # print(y.getKey())

    def preOrderTreeWalk(self, x, _pre):
        if x is not None:
            _pre += str(x.getKey())
            _pre += ' '
            self.preOrderTreeWalk(x.getLeft(), _pre)
            self.preOrderTreeWalk(x.getRight(), _pre)

    def inOrderTreeWalk(self, x, _in):
        if x is not None:
            self.inOrderTreeWalk(x.getLeft(), _in)
            _in += str(x.getKey())
            _in += ' '
            self.inOrderTreeWalk(x.getRight(), _in)

    def postOrderTreeWalk(self, x, _post):
        if x is not None:
            self.postOrderTreeWalk(x.getLeft(), _post)
            self.postOrderTreeWalk(x.getRight(), _post)
            _post += str(x.getKey())
            _post += ' '

    def search(self, k):
        x = self.root
        while x is not None and k != x.getKey():
            if k < x.getKey():
                x = x.getLeft()
            else:
                x = x.getRight()
        return x


saidas =[]
arvore = Tree()
comandos = int(input('N: '))
for i in range(comandos):
    i = input('>>> ').split(' ')
    if i[0] == 'A':
        arvore.insert(Node(int(i[1])))
    elif i[0] == 'B':
        alvo = arvore.search(int(i[1]))
        arvore.delete(alvo)
    elif i[0] == 'C':
        alvo = arvore.search(int(i[1]))
        if alvo.getKey() == arvore.minimum():
            saidas.append(0)
        else:
            saidas.append(arvore.anteccessor(alvo))
    elif i[0] == 'PRE':
        PRE = ''
        x.preOrderTreeWalk(x.root, PRE)
        saidas.append(PRE)
    elif i[0] == 'IN':
        IN = ''
        x.inOrderTreeWalk(x.root, IN)
        saidas.append(IN)
    elif i[0] == 'POST':
        POST = ''
        x.postOrderTreeWalk(x.root, POST)
        saidas.append(POST)
