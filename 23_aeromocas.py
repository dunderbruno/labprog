u"""
O Sindicato das Aeroçoças.

Aluno: Bruno Olimpio dos Santos
"""

import math


class vertex():
    """Class Vertex."""

    def __init__(self, id):
        """Construtor."""
        self.id = str(id)
        self.distance = 0
        self.neighbors = []
        self.edges = {}  # [vertex:distance]

    def __lt__(self, other):
        """Comparison rule to < operator."""
        return (self.distance < other.distance)

    def __repr__(self):
        """Return the vertex id."""
        return self.id

    def addNeighbor(self, vertex):
        """Add a pointer to a vertex at neighbor's list."""
        self.neighbors.append(vertex)

    def addEdge(self, vertex, weight):
        """Destination vertex and weight."""
        self.edges[vertex.id] = weight


def dijkstra(graph, source, destino):
    """Dijkstra's Algorithm."""
    Q = []
    for v in graph:
        v.distance = math.inf
        Q.append(v)
    source.distance = 0
    while Q:
        v = min(Q)  # ítem de Q com menor self.distance
        Q.remove(v)
        for u in v.neighbors:  # para cada vizinho u de v faça:
            new = v.distance + v.edges[u.id]
            if new < u.distance:  # u é o vizinho de v. Na 1 rodada é infinito
                u.distance = new
    return destino.distance


N, M = input("N, M: ").split(" ")
N, M = int(N), int(M)
rotas = [input("Rota %d: " % (i+1)).split(" ") for i in range(M)]
cidades = [vertex(n) for n in range(N)]


for r in rotas:
    cidades[int(r[0])].addNeighbor(cidades[int(r[1])])
    cidades[int(r[1])].addNeighbor(cidades[int(r[0])])
    cidades[int(r[0])].addEdge(cidades[int(r[1])], int(r[2]))
    cidades[int(r[1])].addEdge(cidades[int(r[0])], int(r[2]))

for c in cidades:
    print(c.id, c.neighbors)
