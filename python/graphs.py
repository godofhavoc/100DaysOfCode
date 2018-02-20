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
