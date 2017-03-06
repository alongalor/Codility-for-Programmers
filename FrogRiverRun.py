def solution(X, A):
    lst = [0]*(X+1)
    count = 0
    for i in range(len(A)):
        lst[A[i]] += 1
        if lst[A[i]] == 1:
            count += 1
        if count == X:
            return i
    return -1