"""Levenshtein Distance."""


def levenshtein(A, B):
    """Levenshtein Distance."""
    m = len(A)
    n = len(B)
    M = []

    for x in range(m+1):
        M.append([])
        for y in range(n+1):
            M[x].append((0))

    for i in range(1, m+1):
        M[i][0] = i-1

    for j in range(1, n+1):
        M[0][j] = j-1

    for x in range(1, m+1):
        for y in range(1, n+1):
            if A[x-1] == B[y-1]:
                cost = 0
            else:
                cost = 2

            M[x][y] = min(
                          M[x-1][y-1] + cost,
                          M[x-1][y] + 1,
                          M[x][y-1] + 1,
                          )

    return(M[m][n])


while True:
    a = input()
    b = input()
    print(levenshtein(a, b))
