import math
import numpy as np

def initialize_single_source(G, s):
    for v in G.V:
        v.d = math.inf
        v.pi = None
    s.d = 0

def relax(u, v, w):
    if v.d > u.d + w(u, v):
        v.d = u.d + w(u, v)
        v.pi = u

def bellman_ford(G, w, s):
    initialize_single_source(G, s)
    for i in range(1, G.V):
        for u, v in G.E:
            relax(u, v, w)
    for u, v in G.E:
        if v.d > u.d + w(u, v):
            return False
    return True

def dijkstra(G, w, s):
    initialize_single_source(G, s)
    S = []
    Q = G.V
    while Q:
        u = extract_min(Q)
        S += u
        for v in G.Adj[u]:
            relax(u, v, w)

def extend_shortest_paths(L, W):
    n = len(L)
    l1 = np.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            l1[i][j] = math.inf
            for k in range(n):
                l1[i][j] = min(l[i][j], L[i][k] + W[k][j])
    return l1

def slow_all_pairs_shortest_paths(W):
    n = W.rows
    L = W
    for m in range(1, n - 1):
        lm = extend_shortest_paths(L, W)
    return L
