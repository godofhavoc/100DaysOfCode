def multipop(S, k):
    while S and k > 0:
        s.pop()
        k -= 1

def increment(A):
    i = 0
    while i < A.length and A[i] == 1:
        A[i] = 0
        i = i + 1
    if i < A.length:
        A[i] = 1
