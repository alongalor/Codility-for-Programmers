def solution(N):
    string = bin(N)[2:]
    
    maximum = 0
    count = 0
    
    for i in string:
        if i=='0':
            count += 1
        else:
            maximum = max(maximum, count)
            count = 0
    
    return maximum
