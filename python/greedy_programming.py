from binary_search_tree import TreeNode

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

def huffman(C):
    n = len(C)
    Q = C
    for i in range(1, n):
        x = extract_min(Q)
        y = extract_min(Q)
        z = TreeNode(x.data + y.data, None, x, y)
        insert(Q, z)
    return extract_min(q)

def sublist(s1, s2):
    def get_all_in(one, another):
        for element in one:
            if element in another:
                yield element

    for x1, x2 in zip(get_all_in(s1, s2), get_all_in(s2, s1)):
        if x1 != x2:
            return False

    return True

def greedy_matroid(M, w):
    A = []
    M.S = sorted(M.S, key=lambda x: w(x), reverse=True)
    for x in M.S:
        if sublist((A + [x]), M.I):
            A = A + [x]
    return A

def unit_task_scheduling(a, d, w):
    n = len(a)
    I = []
    for i in n:
        temp = I + [(a[i], d[i])]

        add = True
        for j in len(temp):
            count = sum(x[1] < temp[j][1] for x in temp)
            if j < count:
                add = False
                break

        if add:
            I += [(a[i], d[i])]

    a_tup = zip(a, d)
    diff = sorted(list(set(a_tup) - set(I)), key=lambda x: x[1])
    final = [x[0] for x in sorted(I + diff, key=lambda y: y[1])]

    return final
