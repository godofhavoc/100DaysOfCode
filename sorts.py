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

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = float("-inf")
    total_sum = 0
    for i in range(low, mid+1):
        total_sum += A[i]
        if total_sum > left_sum:
            left_sum = total_sum
            max_left = i

    right_sum = float("-inf")
    total_sum = 0
    for i in range(mid+1, high+1):
        total_sum += A[i]
        if total_sum > right_sum:
            right_sum = total_sum
            max_right = i

    return (max_left, max_right, left_sum + right_sum)

def find_maximum_subarray(A, low, high):
    if high == low:
        return (low, high,  A[low])
    else:
        mid = int((low + high)/2)
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

def quicksort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quicksort(arr, start, pivot - 1)
        quicksort(arr, pivot + 1, end)

def partition(arr, start, end):
    x = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i + 1

def randomized_partition (arr, start, end):
    i = random.randint(start, end)
    arr[r], arr[i] = arr[i], arr[r]
    return partition(arr, start, end)

def quicksort_simple(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort_simple(less) + [pivot] + quicksort_simple(greater)

def counting_sort(arr):
    k = max(arr)
    c = []
    b = []
    for i in range(0, k+1):
        c.append(0)

    for val in arr:
        c[val] += 1
        b.append(None)


    for idx, _ in enumerate(c):
        if idx:
            c[idx] = c[idx] + c[idx - 1]

    print(c)

    for val in reversed(arr):
        b[c[val] - 1] = val
        c[val] -= 1

    return b
