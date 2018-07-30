import math


class vertex():
    """Class Vertex."""

    def __init__(self, id):
        """Construtor."""
        self.id = str(id)
        self.key = None
        self.pi = None
        self.neighbors = []
        self.edges = {}  # [vertex:distance]

    def __lt__(self, other):
        """Comparison rule to < operator."""
        return (self.key < other.key)

    def __repr__(self):
        """Return the vertex id."""
        return self.id

    def addNeighbor(self, vertex):
        """Add a pointer to a vertex at neighbor's list."""
        self.neighbors.append(vertex)

    def addEdge(self, vertex, weight):
        """Destination vertex and weight."""
        self.edges[vertex.id] = weight


def prim(graph, root):
    """Prim's Algorithm."""
    A = []
    for u in graph:
        u.key = math.inf
        u.pi = None
    root.key = 0
    Q = graph[:]
    while Q:
        u = min(Q)
        Q.remove(u)
        for v in u.neighbors:
            if (v in Q) and (u.edges[v.id] < v.key):
                v.pi = u
                v.key = u.edges[v.id]
    for i in graph:
        A.append((i, i.pi))
    return(A)
