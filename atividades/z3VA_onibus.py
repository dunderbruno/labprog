class vertex():
    def __init__(self, id):
        self.id = str(id)
        self.distance = 0
        self.neighbors = []
        self.edges = {}

    def __lt__(self, other):
        return (self.distance < other.distance)

    def addNeighbor(self, vertex):
        self.neighbors.append(vertex)

    def addEdge(self, vertex):
            self.edges[vertex.id] = 1

import math
def dijkstra(graph, source, destiny):
    Q = []
    for v in graph:
        v.distance = math.inf
        Q.append(v)
    source.distance = 0
    while Q:
        v = min(Q)
        Q.remove(v)
        for u in v.neighbors:
            new = v.distance + v.edges[u.id]
            if new < u.distance:
                u.distance = new
    return destiny.distance


N, A, B = input().split(" ")
N, A, B = int(N), int(A), int(B)
rotas = [input().split(" ") for i in range(N-1)]
cidades = [vertex(n) for n in range(N)]

for r in rotas:
    cidades[int(r[0])-1].addNeighbor(cidades[int(r[1])-1])
    cidades[int(r[1])-1].addNeighbor(cidades[int(r[0])-1])
    cidades[int(r[0])-1].addEdge(cidades[int(r[1])-1])
    cidades[int(r[1])-1].addEdge(cidades[int(r[0])-1])


print(dijkstra(cidades, cidades[A-1], cidades[B-1]))