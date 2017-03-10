def solution(A, B):
    down = []
    up = []
    for i in xrange(len(B)):
        if B[i]==1:
            down += [(i, A[i])]
        else:
            up += [(i, A[i])]
        while (len(up)>0 and len(down)>0) and (down[-1][0] < up[-1][0]):
            if down[-1][1] > up[-1][1]:
                up.pop()
            else:
                down.pop()
    return len(up) + len(down)