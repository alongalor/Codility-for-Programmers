def solution(A):
    lst = [0]*len(A)
    for i in A:
        if 1<=i<=len(A):
            lst[i-1] = 1
    for i in xrange(len(lst)+1):
        if lst[i]==0:
            return i+1
    return len(A)+1