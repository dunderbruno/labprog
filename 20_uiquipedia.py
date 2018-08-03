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


N = int(input())
diretas = [input().split(" ") for i in range(N)]

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

for i in range(len(alfabetica)-1):
    referencias[alfabetica[i]].addNeighbor(referencias[alfabetica[i+1]])

for i in diretas:
    referencias[i[0]].addNeighbor(referencias[i[1]])
    referencias[i[1]].addNeighbor(referencias[i[0]])

for r in referencias.values():
    print(r, r.neighbors)
