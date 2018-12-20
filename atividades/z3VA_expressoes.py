class noh:

    def __init__(self, dado):
        self.dado = dado
        self.next = None

    def getDado(self):
        return self.dado

    def getNext(self):
        return self.next

    def setDado(self, dado):
        self.dado = dado

    def setNext(self, next):
        self.next = next


class pilha:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def insertAtBegin(self, value):
        newNode = noh(value)
        if self.isEmpty():
            self.primeiro = self.ultimo = newNode
        else:
            newNode.setNext(self.primeiro)
            self.primeiro = newNode

    def removeFromBegin(self):
        if self.primeiro is self.ultimo:
            self.primeiro = self.ultimo = None
        else:
            self.primeiro = self.primeiro.getNext()


    def isEmpty(self):
        return self.primeiro is None



def definida(tokens):
    parenteses = pilha()
    colchetes  = pilha()
    chaves     = pilha()
    
    for i in tokens:
        if i == '(':
            parenteses.insertAtBegin(i)
        elif i == '[':
            colchetes.insertAtBegin(i)
        elif i == '{':
            chaves.insertAtBegin(i)
            
    for j in tokens:
        if j == ')':
            parenteses.removeFromBegin()
        elif j == ']':
            colchetes.removeFromBegin()
        elif j == '}':
            chaves.removeFromBegin()
    estado='S'
    if parenteses.isEmpty() == False:
        estado = 'N'
    if colchetes.isEmpty() == False:
        estado = 'N'
    if chaves.isEmpty() == False:
        estado = 'N'
    return estado


T = int(input())


saidas = []
for i in range(T):
    entrada = input()
    if entrada == '':
        saidas.append('S')
    else:
        saidas.append(definida(entrada))

for i in saidas:
    print(i)
