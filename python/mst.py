import math

def mst_kruskal(G, w):
    A = []
    for v in G.V:
        make_set(v)
    G.E.sort(key=w)
    for u, v in G.E:
        if find_set(u) != find_set(v):
            A += (u, v)
            union(u, v)
    return A

def mst_prim(G, w, r):
    for u in G.V:
        u.key = math.inf
        u.pi = None

    r.key = 0
    Q = G.V
    while Q != None:
        u = extract_min(Q)
        for v in G.Adj[u]:
            if v in Q and w(u, v) < v.key:
                v.pi = u
                v.key = w(u, v)
