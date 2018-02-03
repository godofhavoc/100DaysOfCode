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

    for val in reversed(arr):
        b[c[val] - 1] = val
        c[val] -= 1

    return b

def bucket_sort(arr):
    n = len(arr)
    b = []
    for i in range(n - 1):
        b[i] = []

    for val in arr:
        b[int(n * val)].append(val)
    for val in b:
        val = insertion_sort(val)

    return [inner for outer in b for inner in outer]

def randomized_select(arr, start, end, i):
    if start == end:
        return arr[start]
    pivot = randomized_partition(arr, start, end)
    k = pivot - p + 1
    if i == k:
        return arr[pivot]
    elif i < k:
        return randomized_select(arr, start, pivot - 1, i)
    else:
        return randomized_select(arr, pivot + 1, end,  i - k)

class Node:
    def __init__(self, data=None, next=None):
        self._data = data
        self.next = next

    def __str__(self):
        return str(self._data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.next:
            return self.next
        else:
            raise StopIteration

    @property
    def data(self):
        return self._data

class TreeNode:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self.parent = parent
        self.left = left
        self.right = right

    @property
    def data(self):
        return self._data

def inorder_tree_walk(x):
    if not x == None:
        inorder_tree_walk(x.left)
        print x.data
        inorder_tree_walk(x.right)

def tree_search(x, k):
    if x == None or k == x.data:
        return x
    if k < x.data:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)

def tree_minimum(x):
    while not x.left == None:
        x = x.left
    return x

def tree_maximum(x):
    while not x.right == None:
        x = x.right
    return x

def tree_successor(x):
    if not x.right == None:
        return tree_minimum(x.right)
    y = x.parent
    while not y == None and x == y.right:
        x = y
        y = y.p
    return y

def tree_insertion(T, z):
    y = None
    x = T.root
    while not x == None:
        y = x
        if z.data < x.data:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == None:
        T.root = z
    elif z.data < y.data:
        y.left = z
    else:
        y.right = z

def transplant(T, u, v):
    if u.parent == None:
        T.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if not v == None:
        v.parent = u.parent

def tree_delete(T, z):
    if z.left == None:
        transplant(T, z, z.right)
    elif z.right == None:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        if not y.parent == z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.parent = y
        transplant(T, z, y)
        y.left = z.left
        y.left.parent = y
