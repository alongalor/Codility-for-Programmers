def solution(A):
    stack = []

    for i in A:
        if stack != []:
            if stack[-1] == i:
                stack += [i] 
            else: 
                stack.pop()
        else:
            stack += [i]
    
    num = -1
    if stack != []:
        num = stack[0]
    
    count = 0 
    idx = -1
    for i in range(len(A)): 
        if A[i] == num:
            count += 1
            idx = i

    if count > len(A)//2:
        return idx
    return -1
