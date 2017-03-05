def solution(A):
    d = {}
    for i in range(1, len(A) + 2):
        d[i] = 1
    
    for i in A:
        d[i] = 0
        
    for key, val in d.iteritems():
        if val == 1:
            return key