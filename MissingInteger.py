def solution(A):
    d = {}
    
    for i in A:
        d[i] = d.get(i, 0) + 1
    
    for i in xrange(1,len(A)+2):
        if d.get(i, 0) == 0:
            return i