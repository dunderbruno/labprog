"""Uiquipedia."""

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


N = int(input())
diretas = [input().split(" ") for i in range(N)]
void = input()
origem, destino = input().split(" ")

alfabetica = []
for i in diretas:
    alfabetica.extend(i)
alfabetica = list(set(alfabetica))
alfabetica.sort()

referencias = {}

for a in alfabetica:
    referencias[a] = vertex(a)

for i in range(1, len(alfabetica)):
    referencias[alfabetica[i]].addNeighbor(referencias[alfabetica[i-1]])
    referencias[alfabetica[i]].addEdge(referencias[alfabetica[i-1]], 1)

for i in range(len(alfabetica)-1):
    referencias[alfabetica[i]].addNeighbor(referencias[alfabetica[i+1]])
    referencias[alfabetica[i]].addEdge(referencias[alfabetica[i+1]], 1)

for i in diretas:
    referencias[i[0]].addNeighbor(referencias[i[1]])
    referencias[i[0]].addEdge(referencias[i[1]], 1)
    referencias[i[1]].addNeighbor(referencias[i[0]])
    referencias[i[1]].addEdge(referencias[i[0]], 1)

# for r in referencias.values():
#     print(r, r.neighbors)

print(dijkstra(referencias.values(), referencias[origem], referencias[destino]))
