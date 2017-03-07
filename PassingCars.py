def solution(A):
    n = len(A)
    sums = [0]*(n+1)
    for i in list(reversed(xrange(1, n+1))):
        sums[i-1] = A[i-1] + sums[i]
    count = 0
    for i in xrange(len(A)):
        if A[i]==0:
            count += sums[i]
    if count <= 1000000000:
        return count
    else:
        return -1