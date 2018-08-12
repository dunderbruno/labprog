class edge():
    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.w = w

    def __lt__(self, other):
        return self.w > other.w


def findset(vertex):
    """Receive a vertex and return the set it belongs."""
    for i in SUPERSET:
        if vertex in i:
            return i


def kruskal(G, w):
    A = []
    SUPERSET = []
    for v in G:
        SUPERSET.append([v])
    w.sort()
    for e in w:
        if findset(e[0]) != findset(e[1]):
            A.append([e])
            w[0].extend(findset(e[1]))
            w[0].remove(e[1])
    return SUPERSET



    # a = [['a'],['b'],['c']]
    # a[0].extend(a[2])
    # a.remove(a[2])
