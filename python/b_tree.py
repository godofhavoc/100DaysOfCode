NO_NODES = 100

class BTreeNode:
    _no_keys = NO_NODES
    _keys = [None] * _no_keys
    _leaf = True
    _children = [None] * _no_keys

    def __init__(self, data=None, children=None):
        if data:
            self._keys = data

        if children:
            self._children = children

        if [x for x in self._children if x is not None]:
            self._leaf = False

    def __len__(self):
        return self._no_keys

    @property
    def key(self):
        return self._keys

    @property
    def leaf(self):
        return self._leaf

    @leaf.setter
    def leaf(self, value):
        self._leaf = False

    @property
    def n(self):
        return _no_keys

    @n.setter
    def n(self, value):
        if self._no_keys:
            if (value < self._no_keys):
                self._keys = self._keys[:value]
                self._children = self._children[:value]
            else:
                extra = [None] * (self._no_keys - value)
                self._keys += extra
                self._children += extra
        else:
            self._keys = [None] * self._no_keys
        self._keys = self._no_keys

    @property
    def c(self):
        return self._children

def b_tree_search(x, k):
    i = 1
    while i < len(x) and k > x.key[i]:
        i += 1
    if i < len(x) and k == x.key[i]:
        return (x, i)
    else if x.leaf:
        return None
    else:
        disk_read(x.c[i])
        return b_tree_search(x.c[i], k)

def b_tree_create(T):
    x = BTreeNode()
    x.leaf = True
    x.n = 0
    disk_write(x)
    T.root = x

def b_tree_split_child(x, i):
    z = BTreeNode()
    y = x.c[i]
    z.leaf = y.leaf
    z.n = t - 1
    for j in range(1, t):
        z.key[j] = y.key[j + t]
    if not y.leaf:
        for j in range(1, t+1):
            z.c[j] = y.c[j + t]
    y.n = t - 1
    for j in range(x.n + 1, i, -1):
        x.c[j + 1] = x.c[j]
    x.c[i + 1] = z
    for j in range(x.n, 0):
        x.key[j + 1] = x.key[j]
    x.key[i + 1] = y.key
    x.n = x.n + 1
    disk_write(y)
    disk_write(z)
    disk_write(x)

def b_tree_insert(T, k):
    r = T.root
    if r.n == 2 * t - 1:
        s = BTreeNode()
        T.root = s
        s.leaf = False
        s.n = 0
        s.c1 = r
        b_tree_split_child(s, 1)
        b_tree_insert_non_full(s, k)
    else:
        b_tree_insert_non_full(r, k)

def b_tree_insert_non_full(x, k):
    i = x.n
    if x.leaf:
        while i >= 1: and k < x.key[i]:
            x.key[i + 1] = x.key[i]
            i -= 1
        x.key[i + 1] = k
        x.n = x.n + 1
    else:
        while i >= 1 and k < x.key[i]:
            i -= 1
        i += 1
        disk_read(x.c[i])
        if x.c[i].n == 2 * t - 1:
            b_tree_split_child(x, i)
            if k > x.key[i]:
                i += 1
        b_tree_insert_non_full(x.c[i], k)

def b_tree_delete(x, k):
    if k in x.key and x.leaf:
        x.key.remove(k)
        x.n -= 1
    else:
        if not x.leaf:
            if k in x.key:
                i = x.key.index(k)
                y = x.c[i - 1]
                y = z.c[i - 1]
                if len(y.key) >= t:
                    j = 0
                    while k > y.key[j]:
                        j += 1
                    x.key[i] = y.key[j]
                    b_tree_delete(y, y.key[j])
                elif len(z.key) >= t:
                    j = 0
                    while k > z.key[j]:
                        j += 1
                    x.key[i] = z.key[j]
                    b_tree_delete(z, z.key[j])
                else:
                    x.n += z.n + 1
                    x.key[x.n + 1] = k
                    for j in range(i, x.n + 1):
                        x.key[j + z.n] = x.key[j]
                        x.child[j + z.n] = x.child[j]
                    for j, l in zip(range(x.n, z.n + 1), zip(1, z.n + 1)):
                        x.key[j] = z.key[l]
                        x.child[j] = z.child[l]
                    b_tree_delete(x, k)
            else:
                i = 1
                while i < n and k > x.key[i]:
                    i += 1
                x.c[i]
