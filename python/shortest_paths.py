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
