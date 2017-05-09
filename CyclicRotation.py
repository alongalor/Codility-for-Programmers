def solution(A, K):
    if len(A)==0:
        return A
    else:
        for i in range(K):
            A = [A[-1]] + A[:-1]
        return A
    
# Alternative Solution

def solution(A,K):
    B = [0]*len(A)
    
    for i in range(len(A)):
        B[(K + i)%len(A)] = A[i]
    
    return B
