def solution(A):
    A = sorted(A)
    return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])