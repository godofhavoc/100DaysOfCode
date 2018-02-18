def proto_veb_member(V, x):
    if V.u == 2:
        return V.A[x]
    else:
        return proto_veb_member(V.cluster[high(x)], low(x))
