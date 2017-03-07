def solution(A):
    if len(A)==0 or len(A)==1:
        return len(A)
    A.sort() 
    count = 1
    for i in xrange(len(A)-1):
        if A[i+1] != A[i]:
            count += 1
    return count