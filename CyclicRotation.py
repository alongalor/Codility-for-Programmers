def solution(A, K):
    if len(A)==0:
        return A
    else:
        for i in range(K):
            temp = []
            temp += [A[-1]] + A[:-1]
            A = temp
        return A