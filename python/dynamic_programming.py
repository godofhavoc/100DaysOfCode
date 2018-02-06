import math

def cut_rod(p, n):
    if n == 0:
        return 0
    q = -math.inf
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n-i))
    return q

def memoized_cut_rod(p, n):
    r = []
    for i in range(0, n+1):
        r.append(-math.inf)
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -math.inf
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n-i, r))
    r[n] = q
    return q

def bottom_up_cut_rod(p, n):
    r = [0]
    for j in range(1, n+1):
        q = -math.inf
        for i in range(1, j):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]
