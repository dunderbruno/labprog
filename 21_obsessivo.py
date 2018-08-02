u"""
Juvenal é obsessivo-compulsivo

Aluno: Bruno Olimpio dos Santos
"""

import math


class vertex():
    """Class Vertex."""

    def __init__(self, id):
        u"""
        Classe vertex é iniciada com argumento id.

        >>> x = vertex(8)

        Arguments:
            id - identifier of object.

        Atributes:
            distance  - to be used by dijkstra function
            neighbors - list to add pointers to neighbors
            edges     - dictionary: [vertex:weight]
        """
        self.id = str(id)
        self.distance = 0
        self.neighbors = []
        self.edges = {}

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
    vertices = 0
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
                vertices += 1
    if vertices // 2 == 0:
        return destino.distance
    else:
        return -1


C, V = input().split(" ")
C, V = int(C), int(V)
rotas = [input().split(" ") for i in range(V)]
cidades = [vertex(n) for n in range(1, C+1)]

for r in rotas:
    cidades[int(r[0])].addNeighbor(cidades[int(r[1])])
    cidades[int(r[1])].addNeighbor(cidades[int(r[0])])
    cidades[int(r[0])].addEdge(cidades[int(r[1])], int(r[2]))
    cidades[int(r[1])].addEdge(cidades[int(r[0])], int(r[2]))

print(dijkstra(cidades, cidade[0], cidade[C]))
