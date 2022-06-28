from collections import defaultdict
from collections import deque
from heapq import heappush, heappop

def buildgraph(filnavn):
    V = set()
    E = defaultdict(set)
    w = dict()
    lines = open(filnavn)
    for line in lines:
        v,u,weight = line.strip().split()
        V.add(v)
        V.add(u)

        E[v].add(u)
        E[u].add(v)

        w[(v,u)] = int(weight)
        w[(u,v)] = int(weight)
    lines.close()
    return V,E,w

def visualiserGraf(G):
    V, E , w  = G
    for edges in E:
        print(edges)

def dfs(G,s):
    _,E,_ = G
    visited = set()
    stack = [s]
    result = []
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        result.append(v)
        visited.add(v)
        for u in E[v]:
            stack.append(v)
    return result

def dfs_rec(G,s,visited, result):
    _,E,_ = G
    result.append(s)
    visited.add(s)
    for v in E[s]:
        if v not in visited:
            dfs_rec(G,v,visited,result)
    return result

def bfs(G, s):
    _, E, _ = G
    visited = set([s])
    queue = deque([s])
    result = []

    while queue:
        v = deque.popleft(queue)
        result.append(v)
        for u in E[v]:
            if u not in visited:
                visited.add(u)
                queue.append(u)
    return result

def bfs_shortest_paths_from(G, s):
    _, E, _ = G
    parents = {s : None}
    queue = deque([s])
    result = []

    while queue:
        v = deque.popleft(queue)
        result.append(v)
        for u in E[v]:
            if u not in parents:
                parents[u] = v
                queue.append(u)
    return parents

def bfs_shortest_path_between(G, s, t):
    parents = bfs_shortest_paths_from(G, s)
    v = t
    path = []

    if t not in parents:
        return path

    while v:
        path.append(v)
        v = parents[v]
    return path[::-1]

def bfs_all_shortest_paths(G, s):
    V, _, _ = G
    parents = bfs_shortest_paths_from(G, s)
    paths = []

    for v in V:
        path = []
        while v:
            path.append(v)
            v = parents[v]
        paths.append(path[::-1])
    return paths

def dijkstra(G, s):
    V, E, w = G
    Q = [(0, s)]
    D = defaultdict(lambda: float('inf'))
    D[s] = 0

    while Q:
        cost, v = heappop(Q)
        for u in E[v]:
            c = cost + w[(v, u)]
            if c < D[u]:
                D[u] = c
                heappush(Q, (c, u))

    return D

# Kjører shortest paths etter å ha utført dijkstra prosedyren
def shortest_paths_from(G, s):
    V, E, w = G
    Q = [(0, s)]
    D = defaultdict(lambda: float('inf'))
    parents = {s : None}
    D[s] = 0

    while Q:
        cost, v = heappop(Q)
        for u in E[v]:
            c = cost + w[(v, u)]
            if c < D[u]:
                D[u] = c
                heappush(Q, (c, u))
                parents[u] = v

    return parents

def prim(G):
    V, E, w = G
    # Pick arbitrary start vertex
    s = next(iter(V))
    Q = [(0, s, None)]
    parents = dict()

    while Q:
        _, v, p = heappop(Q)
        if v in parents:
            continue
        parents[v] = p

        for u in E[v]:
            heappush(Q, (w[(v, u)], u, v))

    return parents

#
def removenode(G, v):
    V, E, w = G

    newV = V.copy()
    newE = E.copy()

    newV.discard(v)
    del newE[v]

    for u in newV:
        neighbors = newE[u].copy()
        neighbors.discard(v)
        newE[u] = neighbors

    return newV, newE, w

def isbiconnected_naive(G):
    V, E, _ = G
    for v in V:
        newV, _, _ = newG = removenode(G, v)
        nodelist = dfs(newG, next(iter(newV)))
        if set(nodelist) != newV:
            return False
    return True

def separationnodes_rec(E, u, d, depth, low, seps):
    depth[u] = low[u] = d
    for v in E[u]:
        if v in depth:
            low[u] = min(low[u], depth[v])
            continue
        separationnodes_rec(E, v, d + 1, depth, low, seps)
        low[u] = min(low[u], low[v])
        if d <= low[v]:
            seps.add(u)

def separationnodes(G):
    V, E, _ = G
    s = next(iter(V))
    depth = {s: 0}
    low = {s: 0}
    seps = set()

    for u in E[s]:
        if u not in depth:
            separationnodes_rec(E, u, 1, depth, low, seps)

    if len([u for u in E[s] if depth[u] == 1]) > 1:
        seps.add(s)

    return seps

def isbiconnected(G):
    return len(separationnodes(G)) == 0


def main():
    G = buildgraph("test.txt")
    visualiserGraf(G)

main()
    # DFS-Søk
    # dfs_rec(G, 'A', set(), []) 
    # dfs(G, 'A')

    # BFS-Søk
    # bfs(G, 'A')
    # bfs_shortest_path_between(G, 'A', 'G')
    # sorted(bfs_all_shortest_paths(G, 'A'))
    # draw_parents(bfs_shortest_paths_from(G, 'A'))

    # Dijkstra
    # D = dijkstra(G, 'A')
    # list(zip(*sorted(D.items())))
    # draw_parents_weighted(G, shortest_paths_from(G, 'A'), 'dijkstra_spanningtree')

    # Bikonnektivitet
    # isbiconnected_naive(G) # True
    # isbiconnected_naive(removenode(G, 'C')) # False

    # Separasjonsnoder
    # separationnodes(G)
    # sorted(separationnodes(removenode(G, 'C')))
    # isbiconnected(G) # True
    # isbiconnected(removenode(G, 'C')) # False






