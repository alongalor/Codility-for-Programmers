def solution(A):
    m = len(A)+1
    lst = [0]*m
    
    for i in A:
        if i<m:
            lst[i] = 1
            
    return 0 if 0 in lst[1:] else 1
