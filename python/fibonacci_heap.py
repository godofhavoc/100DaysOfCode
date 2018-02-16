class Node:
    _parent = None
    _child = None
    _left = None
    _right = None
    _degree = 0
    _mark = False

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

class FibonacciHeap:
    _min = None

    def __init__(self, minimum=None):
        self._min = minimum

    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, value):
        self._min = value
