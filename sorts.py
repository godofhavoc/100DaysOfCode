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
