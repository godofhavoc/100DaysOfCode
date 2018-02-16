import math

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

    @property
    def degree(self):
        return self._degree

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

def fib_heap_extract_min(H):
    z = H.min
    if z != None:
        for x in z.child:
            H.root_list.append(x)
            x.parent = None
        H.root_list.remove(z)
        if z == z.right:
            H.min = None
        else:
            H.min = z.right
            consolidate(H)
        H.n = H.n - 1
    return z

def consolidate(H):
    A = [None] * (D(H.n) + 1)

    for w in H.root_list:
        x = w
        d = x.degree
        while A[d] != None:
            y = A[d]
            if x.key > y.key:
                x, y = y, x
            fib_heap_link(H, y, x)
            A[d] = None
            d += 1
        A[d] = x
    H.min = None
    for i in range(0, D(H.n) + 1):
        if A[i] != None:
            if H.min == None:
                H.root_list = [A[i]]
                H.min = A[i]
            else:
                H.root_list.append(A[i])
                if A[i].key < H.min.key:
                    H.min = A[i]

def fib_heap_link(H, y, x):
    H.root_list.remove(y)
    if x.child:
        x.child.append(y)
    else:
        x.child = [y]
    x.degree += 1
    y.mark = False

def fib_heap_decrease_key(H, x, k):
    if k > x.key:
        print('new key is greater than current')
    x.key = k
    y = x.p
    if y != None and x.key < y.key:
        cut(H, x, y)
        cascading_cut(H, y)
    if x.key < H.min.key:
        H.min = x

def cut(H, x, y):
    y.child.remove(x)
    y.degree -= 1
    H.root_list.add(x)
    x.p = None
    x.mark = False

def cascading_cut(H, y):
    z = y.parent
    if z != None:
        if y.mark == False:
            y.mark = True
        else:
            cut(H, y, z)
            cascading_cut(H, z)

def fib_heap_delete_key(H, x):
    fib_heap_delete_key(H, x, -math.inf)
    fib_heap_extract_min(H)
