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
    x.

class test:
    _x = 12
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
