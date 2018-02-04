class TreeNode:
    def __init__(self, data=None, parent=None, left=None, right=None, color=None):
        self._data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color

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
