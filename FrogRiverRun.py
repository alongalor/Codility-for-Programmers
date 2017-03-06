def solution(X, A):
    lst = [0]*X
    count = 0
    i = 0
    while count < X:
        if i==len(A):
            return -1
        lst[A[i]-1] += 1
        i += 1
        if lst[A[i-1]-1] == 1:
            count += 1
    return i-1