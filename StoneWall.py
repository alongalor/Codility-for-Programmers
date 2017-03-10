def solution(H):
    count = 0
    stack = []
    for i in xrange(0,len(H)):
        while len(stack) != 0 and H[i] < stack[-1]:
            stack.pop()
        if len(stack) != 0 and H[i] == stack[-1]:
                count += 1 
                stack.pop()
        if i < len(H)-1:
            if H[i] == H[i+1]:
                count += 1
            if H[i+1] > H[i]:
                stack += [H[i]]
    return len(H) - count
