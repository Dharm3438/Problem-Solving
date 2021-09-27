def performOps(A):
    blen = 2 * len(A)
    B = [0]*blen
    for i in range(len(A)):
        B[i] = A[i]
        B[i + len(A)] = A[(len(A) - i) % len(A)]
    return B

B = performOps([5, 10, 2, 1])
for i in range(len(B)):
    print(B[i])