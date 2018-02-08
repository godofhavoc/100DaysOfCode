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
    r = [None] * n
    r[0] = 0
    for j in range(1, n+1):
        q = -math.inf
        for i in range(1, j):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]

def extended_bottom_up_cut_rod(p, n):
    r = [None] * (n + 1)
    s = [None] * (n + 1)
    r[0] = 0
    for j in range(1, n+1):
        q = -math.inf
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
            s[j] = i
        r[j] = q
    return r and s

def print_cut_rod(p, n):
    r, s = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print s[n]
        n = n - s[n]

def matrix_multiply(A, B):
    if not len(A[0]) == len(B):
        print 'incompatible dimensions'
    else:
        c = [[None for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                c[i][j] = 0
                for k in range(len(A[0])):
                    c[i][j] += a[i][k] * b[k][j]
        return c
