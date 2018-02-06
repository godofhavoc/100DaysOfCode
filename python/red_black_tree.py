class TreeNode:
    def __init__(self, data=None, parent=None, left=None, right=None, color=None):
        self._data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color
        self.size = self.right.size + self.left.size + 1

    @property
    def data(self):
        return self._data

def left_rotate(T, x):
    y = x.right
    x.right = y.left
    if not y.left == None:
        y.left.parent = x
    y.parent = x.parent
    if x.parent == None:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y

def right_rotate(T, x):
    y = x.left
    x.left = y.right
    if not y.right == None:
        y.right.parent = x
    y.parent = x.parent
    if x.parent = None:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.right = x
    x.parent = y

def rb_insert(T, z):
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
    z.left = None
    z.right = None
    z.color = 'RED'
    rb_insert_fixup(T, z)

def rb_insert_fixup(T, z):
    while z.parent.color == 'RED':
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y.color == 'RED':
                z.parent.color = 'BLACK'
                y.color = 'BLACK'
                z.parent.parent.color = 'RED'
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    left_rotate(T, z)
                z.parent.color = 'BLACK'
                z.parent.parent.color = 'RED'
                right_rotate(T, z.parent.parent)
        else:
            y = z.parent.parent.left
            if y.color == 'BLACK':
                z.parent.color = 'BLACK'
                y.color = 'BLACK'
                z.parent.parent.color = 'RED'
                z = z.parent.parent
            else:
                if z == z.parent.left:
                    z = z.parent
                    right_rotate(T, z)
                z.parent.color = 'BLACK'
                z.parent.parent.color = 'RED'
                left_rotate(T, z.parent.parent)
    T.root.color = 'BLACK'

def rb_transplant(T, u, v):
    if u.parent == None:
        T.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v:
    v.parent = u.parent

def rb_delete(T, z):
    y = z
    y_original_color = y.color
    if z.left == None:
        x = z.right
        rb_transplant(T, z, z.right)
    elif z.right == None:
        x = z.left
        rb_transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        y_original_color = y.color
        x = y.right
        if y.parent == z:
            x.parent = y
        else:
            rb_transplant(T, y, y.right)
            y.right = z.right
            y.right.parent = y
        rb_transplant(T, z, y)
        y.left = z.left
        y.left.parent = y
        y.color = z.color
    if y_original_color == 'BLACK':
        tb_delete_fixup(T, x)

def rb_delete_fixup(T, x):
    while not x == T.root and x.color == 'BLACK':
        if x == x.parent.left:
            w = x.parent.right
            if w.color == 'RED':
                w.color = 'BLACK'
                x.p.color = 'RED'
                left_rotate(T, x.parent)
                w = x.parent.right
            if w.left.color == 'BLACK' and w.right.color = 'BLACK':
                w.color = 'RED'
                x = x.parent
            else:
                if w.right.color == 'BLACK':
                    w.left.color = 'BLACK'
                    w.color = 'RED'
                    right_rotate(T, w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = 'BLACK'
                w.right.color = 'BLACK'
                left_rotate(T, x.parent)
                x = T.root
        else:
            w = x.parent.right
            if w.color == 'RED':
                w.color = 'BLACK'
                x.parent.color = 'RED'
                right_rotate(T, x.parent)
                w = x.parent.left
            if w.right.color == 'BLACK' and w.left.color == 'BLACK':
                w.color = 'RED'
                x = x.parent
            else:
                if w.left.color = 'BLACK':
                    w.right.color = 'BLACK'
                    w.color = 'RED'
                    left_rotate(T, w)
                    w = x.parent.left
                w.color = x.parent.color
                x.parent.color = 'BLACK'
                w.left.color = 'BLACK'
                right_rotate(T, x.parent)
                x = T.root
    x.color = 'BLACK'

def os_select(x, i):
    r = x.left.size + 1
    if i == r:
        return x
    elif i < r:
        return os_select(x.left, i)
    else:
        return os_select(x.right, i)

def os_rank(T, x):
    r = x.left.size + 1
    y = x
    while not y == T.root:
        if y == y.parent.right:
            r += y.parent.left.size + 1
        y = y.parent
    return r
