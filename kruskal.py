def findset(vertex):
    """Receive a vertex and return the set it belongs."""
    for i in SUPERSET:
        if vertex in i:
            return i

def union(u, v):
    pass

def kruskal(G, w):
    A = []
    SUPERSET = []
    for v in G:
        SUPERSET.append([v])
    w.sort(key=peso)
    for e in w:
        if findset(e[0]) != findset(e[1]):
            A += e
            union(u, v)
    return A
