def solution(A):
    s = sum(A)
    num = 0
    minimum = float('inf')
    
    for i in range(len(A)-1):
        num += A[i]
        result = abs(2*num - s)
        minimum = min(result, minimum)
    return minimum
