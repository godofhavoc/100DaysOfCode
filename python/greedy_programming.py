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
