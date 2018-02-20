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

def proto_veb_minimum(V):
    if V.u == 2:
        if V.A[0]:
            return 0
        elif V.A[1]:
            return 1
        else:
            return None
    else:
        min_cluster = proto_veb_minimum(V.summary)
        if min_cluster == None:
            return None
        else:
            offset = proto_veb_minimum(V.cluster[min_cluster])
            return index(min_cluster, offset)

def proto_veb_successor(V, x):
    if V.u == 2:
        if x == 0 and V.A[1] == 1:
            return 1
        else:
            return None
    else:
        offset = proto_veb_successor(V.cluster[high(x)], low(x))
        if offset != None:
            return index(high(x), offset)
        else:
            succ_cluster = proto_veb_successor(V.summary, high(x))
            if succ_cluster == None:
                return None
            else:
                offset = proto_veb_minimum(V.cluster[succ_cluster])
                return index(succ_cluster, offset)

def proto_veb_insert(V, x):
    if V.u == 2:
        V.A[x] = 1
    else:
        proto_veb_insert(V.cluster[high(x)], low(x))
        proto_veb_insert(V.summary, high(x))
