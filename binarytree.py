"""Binary Search Tree."""


class No():
    """Class Node."""

    def __init__(self, chave, dado):
        """Init."""
        self.dado = dado
        self.chave = chave
        self.pai = None
        self.esq = None
        self.dir = None

    def getDado(self):
        return self.dado

    def setDado(self, dado):
        self.dado = dado

    def getChave(self):
        return self.chave

    def setChave(self, chave):
        self.chave = chave

    def getPai(self):
        return self.pai

    def setPai(self, pai):
        self.pai = pai

    def getEsq(self):
        return self.esq

    def getDir(self):
        return self.dir

    def setEsq(self, novo):
        self.esq = novo

    def setDir(self, novo):
        self.dir = novo


class tree():
    """Binary Serarch Tree."""
    def __init__(self, raiz):
        self.raiz = raiz

    def isEmpty(self):
        """Retorna True se vazio."""
        return self.raiz == None

    def getRaiz(self):
        return self.raiz

    def inserir(self, chave, dado=None):
        novono = No(chave, dado)
        if self.isEmpty():
            self.raiz = novono
        else:
            i = self.raiz
            while i is not None:
                if chave < i.getChave():
                    if i.getEsq() is not None:
                        i = i.getEsq()
                    else:
                        i.setEsq(novono)
                        novono.setPai(i)
                        break
                else:
                    if i.getDir() is not None:
                        i = i.getDir()
                    else:
                        i.setDir(novono)
                        novono.setPai(i)
                        break

    def buscar(self, k):
        i = self.raiz
        while i is not None:
            if i.getChave() == k:
                return i
            else:
                if k < i.getChave():
                    i = i.getEsq()
                else:
                    i = i.getDir()

        # def minimo(self):
        #     i = self.raiz
        #     while i is not None:
        #         if i.getEsq() is not None:
        #             i = i.getEsq()
        #         else:
        #             return i

    def minimo(self, i):
        u"""
        Minimo de uma sub-arvore.

        i é o ponto de partida.
        Para saber o mínimo da arvore, chamar com i = raiz
        exemplo: minimo(raiz).
        """
        if i is not None:
            while i.getEsq() is not None:
                i = i.getEsq()
            return i

    def maximo(self, i):
        u"""Máximo de uma sub-arvore."""
        if i is not None:
            while i.getDir() is not None:
                i = i.getDir()
            return i

    def sucessor(self, x):
        """
        Sucessor.

        Para fazer antecessor:
        TROCAR MINIMO POR MAXIMO E DIREITA POR ESQUERDA.
        """
        if x is not None:
            if x.getDir() is not None:
                return self.minimo(x.getDir())
        else:
            pai = x.getPai()
            while pai is not None and x is pai.getDir():
                x = pai
                pai = x.getPai()
            return pai

    def preOrdem(self, no):
        if no is not None:
            print(no.getChave())
            self.preOrdem(no.getEsq())
            self.preOrdem(no.getDir())

    def emOrdem(self, no):
        if no is not None:
            self.emOrdem(no.getEsq())
            print(no.getChave())
            self.emOrdem(no.getDir())

    def posOrdem(self, no):
        if no is not None:
            self.posOrdem(no.getEsq())
            self.posOrdem(no.getDir())
            print(no.getChave())

    def populate(self, first, last):
        self.raiz = No(last//2, None)
        for i in range(last//2, first, -1):
            self.inserir(i)
        for i in range((last//2) + 1, last):
            self.inserir(i)
