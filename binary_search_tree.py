class TreeNode:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self.parent = parent
        self.left = left
        self.right = right

    @property
    def data(self):
        return self._data

def inorder_tree_walk(x):
    if not x == None:
        inorder_tree_walk(x.left)
        print x.data
        inorder_tree_walk(x.right)

def tree_search(x, k):
    if x == None or k == x.data:
        return x
    if k < x.data:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)

def tree_minimum(x):
    while not x.left == None:
        x = x.left
    return x

def tree_maximum(x):
    while not x.right == None:
        x = x.right
    return x

def tree_successor(x):
    if not x.right == None:
        return tree_minimum(x.right)
    y = x.parent
    while not y == None and x == y.right:
        x = y
        y = y.p
    return y

def tree_insertion(T, z):
    y = None
    x = T.root
    while not x == None:
        y = x
        if z.data < x.data:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == None:
        T.root = z
    elif z.data < y.data:
        y.left = z
    else:
        y.right = z

def transplant(T, u, v):
    if u.parent == None:
        T.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if not v == None:
        v.parent = u.parent

def tree_delete(T, z):
    if z.left == None:
        transplant(T, z, z.right)
    elif z.right == None:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        if not y.parent == z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.parent = y
        transplant(T, z, y)
        y.left = z.left
        y.left.parent = y
