def ford_fulkerson_method(G, s, t):
    f = 0
    while p in G:
        augment(f, p)
    return f

def whyagain():
    pass
