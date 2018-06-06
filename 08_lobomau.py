# -*- coding: utf-8 -*-

u"""
Lobo Mau.

Aluno: Bruno Olimpio dos Santos.
e-mail: belbrunosantos@gmail.com
"""


class pin:
    """Representa cada coordenada no mapa."""

    def __init__(self, who, x, y):
        """Construtor."""
        self.who = who
        self.x = x
        self.y = y

    def __repr__(self):
        return self.who

    def __eq__(self, i):
        return self.who == i


fazenda = ['.###.#####..',
           '#.kk#...#v#.',
           '#..k#.#.#.#.',
           '#..##k#...#.',
           '#.#v#k###.#.',
           '#..#v#....#.',
           '#...v#v####.',
           '.####.#vv.k#',
           '.......#####']

altura = 9
largura = 12

# CRIA NOVA LISTA COM CARACTERES EM FORMATO DE OBJETOS
mapa = []
for x in range(altura):
    mapa.append([])
    for y in range(largura):
        mapa[-1].append(pin(fazenda[x][y], x, y))

for j in mapa:
    print(j)

# hor = []
# for i in range(len(mapa)):
#    for j in range(len(mapa[i])):
#        if (mapa[i][j] == ('.')) or (mapa[i][j] == ('k')) or (mapa[i][j] == ('v')) and (mapa[i][j-1]=='#' or j == 0):
#            hor.append([])
#        if (mapa[i][j] == ('.')) or (mapa[i][j] == ('k')) or (mapa[i][j] == ('v')):
#            hor[-1].append(mapa[i][j])

# VARREDURA HORIZONTAL
# hor = []
# buscar = ['.','k','v']
# for i in range(len(mapa)):
#    for j in range(len(mapa[i])):
#        if mapa[i][j] in buscar and (mapa[i][j-1]=='#' or j == 0):
#            hor.append([])
#        if (mapa[i][j] in buscar):
#            hor[-1].append(mapa[i][j])
# # print(hor,len(hor))
# # for z in hor:
# #     print(z)
#
# # VARREDURA VERTICAL
# ver = []
# for i in range(largura):
#     for j in range(altura):
#         # print(m[j][i])
#         if mapa[j][i] in buscar and (mapa[j-1][i]=='#' or j==0):
#             # print(m[j][i], 'i:',i,'j:',j)
#             ver.append([])
#         if mapa[j][i] in buscar:
#             ver[-1].append(mapa[j][i])
# # print(ver,len(ver))
# cruzamento = []
# for v in ver:
#     for h in hor:
#         if h in v:
#             print(v+h)
