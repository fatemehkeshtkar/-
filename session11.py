from collections import deque


def BFS(g, s):
    q = deque([s])
    seen = {s}

    while q:
        v = q.popleft()
        for nb in g[v]:
            if nb not in seen:
                seen.add(nb)
                q.append(nb)

    return seen


def DFS(g, s, seen=None):
    if seen is None:
        seen = set()

    seen.add(s)
    for nb in g[s]:
        if nb not in seen:
            DFS(g, nb, seen)

    return seen


def sort1(arr):
    a = arr.copy()
    res = []

    while a:
        m = min(a)
        res.append(m)
        a.remove(m)

    return res


def Bubble(arr):
    a = arr.copy()

    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a