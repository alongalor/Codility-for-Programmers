def solution(A, K):
    if len(A)==0:
        return A
    else:
        for i in range(K):
            A = [A[-1]] + A[:-1]
        return A