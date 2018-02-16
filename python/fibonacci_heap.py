class Node:
    _parent = None
    _child = None
    _left = None
    _right = None
    _degree = 0
    _mark = False
    _key = None

    def __init__(self):
        pass

    @propery
    def p(self):
        return self._parent

    @property
    def child(self):
        return self._child

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

class FibonacciHeap:
    _min = None
    root_list = []

    def __init__(self, minimum=None):
        self._min = minimum

    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, value):
        self._min = value

def fib_heap_insert(H, x):
    x.degree = 0
    x.p = None
    x.child = None
    x.mark = False
    if H.min == None:
        H.root_list = [x]
        H.min = x
    else:
        H.root_list.append(x)
        if x.key < H.min.key:
            H.min = x
    H.n = H.n + 1

def fib_heap_union(H1, H2):
    H = FibonacciHeap()
    H.min = H1.min
    H.root_list += H2.root_list
    if (H1.min == None) or (H2.min != None and H2.min.key < H1.min.key):
        H.min = H2.min
    H.n = H1.n + H2.n
    return H
