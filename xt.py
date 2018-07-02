from binarytree import *

x = tree(None)

x.populate(1,15)

print(x.raiz.getChave())
print('Em')
print(x.emOrdem(x.raiz))
print('Pre')
print(x.preOrdem(x.raiz))
print('Pós')
print(x.posOrdem(x.raiz))
