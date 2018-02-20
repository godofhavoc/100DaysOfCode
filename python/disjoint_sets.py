def connected_components(G):
    for v in G.V:
        make_set(v)
    for e in G.E:
        if find_set(u) != find_set(v):
            union(u, v)

def same_component(u, v):
    if find_set(u) == find_set(v):
        return True
    else:
        return False

class Node:
    __rank = 0
    _parent = None

    def __init__(self, rank=0, parent=None):
        self.__rank = rank
        self._parent = parent

    @property
    def p(self):
        return self._parent

    @p.setter
    def p(self, value):
        self._parent = value

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, value):
        self.__rank = value

def make_set(x1):
    x = Node(0, x)
    return x

def union(x, y):
    link(find_set(x), find_set(y))

def link(x, y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1

def find_set(x):
    if x != x.p:
        x.p = find_set(x.p)
    return x.p
