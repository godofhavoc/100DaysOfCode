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

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[None for _ in range(n)] for _ in range(n)]
    s = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m[i, i] = 0

    for l in range(1, n):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i, j] = math.inf
            for k in range(i, j):
                q = m[i, k] + m[k+1, j] + p[i-1]p[k]p[j]
                if q < m[i, j]:
                    m[i, j] = q
                    s[i, j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print 'A', i
    else:
        print '('
        print_optimal_parens(s, i, s[i, j])
        print_optimal_parens(s, s[i, j] + 1, j)
        print ')'

def memoized_matrix_chain(p):
    n = len(p) - 1
    m = [[None for _ in range(n)] for _ in range(n)]
    for i in range(1, n+1):
        for j in range(i, n):
            m[i, j] = math.inf
    return lookup_chain(m, p, 1, n)

def lookup_chain(m, p, i, j):
    if m[i, j] < math.inf:
        return m[i, j]
    if i == j:
        m[i, j] = 0
    else:
        for k in range(i, j):
            q = lookup_chain(m, p, i, k) + lookup_chain(m, p, k+1, j) + p[i-1]*p[k]*p[j]
        if q < m[i, j]:
            m[i, j] = q
    return m[i, j]

def lcs_length(x, y):
    m = len(x)
    n = len(y)
    b = [[None for _ in range(1, n + 1)] for _ in range(1, m + 1)]
    c = [[None for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        c[i, 0] = 0
    for i in range(n + 1):
        c[0, j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[:i] == y[:i]:
                c[i, j] = c[i - 1, j - 1] + 1
                b[i, j] = 'lu'
            elif c[i - 1, j] >= c[i, j - 1]:
                c[i, j] = c[i - 1, j]
                b[i, j] = 'u'
            else:
                c[i, j] = c[i, j - 1]
                b[i, j] = 'l'
    return c, b

def print_lcs(b, x, i, j):
    if (i == 0) || (j == 0):
        return
    if b[i, j] == 'lu':
        print_lcs(b, x, i - 1, j - 1)
        print x[i]
    elif b[i, j] == 'u':
        print_lcs(b, x, i - 1, j)
    else:
        print_lcs(b, x, i, j - 1)

def optimal_bst(p, q, n):
    e = [[None for _ in range(n + 1)] for _ in range(1, n + 2)]
    w = [[None for _ in range(n + 1)] for _ in range(1, n + 2)]
    root = [[None for _ in range(1, n + 1)] for _ in range(1, n + 1)]
    for i in range(1, n + 2):
        e[i, i - 1] = q[i - 1]
        w[i, i - 1] = q[i - 1]
    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            e[i, j] = math.inf
            w[i, j] = w[i, j - 1] + p[j] + q[j]
            for r in range(i, j + 1):
                t = e[i, r - 1] + e[r + 1, j] + w[i, j]
                if t < e[i, j]:
                    e[i, j] = t
                    root[i, j] = r
    return e, root

def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m <= n && s[m] < f[k]:
        m = m + 1
    if m <= n:
        return a[m] + recursive_activity_selector(s, f, m, n)
    return []

def greedy_activity_selector(s, f):
    n = s.length
    A = [a[0]]
    k = 1
    for m in range(2, n + 1):
        if s[m] >= f[k]:
            A += [a[m]]
            k = m
    return A
