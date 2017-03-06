def solution(A):
    lst = [0]*len(A)
    for i in range(len(A)): 
        if 1<=i<=len(A):
            lst[A[i]-1] += 1  
    if 0 in lst:
        return 0
    else: 
        return 1