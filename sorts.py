import math

def insertion_sort(a):
    for j, value in enumerate(a):
        if j == 0:
            continue
        i = j - 1
        while (i >= 0 and a[i] > value):
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = value

    return a

def merge(a, p, q, r):
    l1 = a[p:q]
    l1.append(math.inf)
    l2 = a[q:r]
    l2.append(math.inf)
    i = 0
    j = 0
    for k in range(r):
        if l1[i] > l2[j]:
            a[k] = l1[i]
            i += 1
        else:
            a[k] = l2[j]
            j += 1

def merge_sort(a, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)
    else:
        return a
