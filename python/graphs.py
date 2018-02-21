import math

WHITE = 'white'
BLACK = 'black'
GRAY = 'gray'

def BFS(s):
    for u in G.V and u != s:
        u.color = WHITE
        u.d = math.inf
        u.pi = None

    s.color = GRAY
    s.d = 0
    s.pi = None
    Q = None
    enqueue(Q, s)
    while Q != None:
        u = dequeue(Q)
        for v in G.Adj[u]:
            if v.color == WHITE:
                v.color = GRAY
                v.d = u.d + 1
                v.pi = u
                enqueue(Q, v)
        u.color = BLACK

def print_path(G, s, v):
    if v == s:
        print(s)
    elif v.pi == None:
        print('no path from ' + s + ' to ' + v + ' exists')
    else:
        print_path(G, s, v.pi)
        print(v)

def dfs(G):
    for u in G.V:
        u.color = WHITE
        u.pi = None
    time = 0
    for u in G.V:
        if u.color == WHITE:
            dfs_visit(G, u)

def dfs_visit(G, u):
    time += 1
    u.d = time
    u.color = GRAY
    for v in G.Adj[u]:
        if v.color == WHITE:
            v.pi = u
            dfs_visit(G, v)
    u.color = BLACK
    time += 1
    u.f = time

def topological_sort(G):
    top = []

    for u in G.V:
        u.color = WHITE
        u.pi = None
    time = 0
    for u in G.V:
        if u.color == WHITE:
            dfs_visit(G, u)
            top.append(u)

    return u
