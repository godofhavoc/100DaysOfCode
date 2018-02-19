import math

u = 256

def high(x):
    return math.floor(x/math.sqrt(u))

def low(x):
    return x % math.sqrt(x)

def index(x, y):
    return x * math.sqrt(x) + y

def proto_veb_member(V, x):
    if V.u == 2:
        return V.A[x]
    else:
        return proto_veb_member(V.cluster[high(x)], low(x))
