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
