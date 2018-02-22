import math

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
