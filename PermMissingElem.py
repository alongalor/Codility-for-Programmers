def solution(A):
    return reduce(lambda x,y: x + y, range(len(A) + 2)) - sum(A)

# Alternative Solution

def solution(A):
    lst = [0]*(len(A)+1)
    for i in A:
        lst[i-1] = 1
    for i in xrange(len(lst)+1):
        if lst[i]==0:
            return i+1
