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
