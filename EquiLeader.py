def solution(A):
    leader, tot_count = goldenLeader_return_count(A)
    
    if leader == -1:
        return 0
    
    current_count = 0
    equi_leaders = 0 
    
    for i in range(len(A)):
        if A[i] == leader:
            current_count += 1
        
        if (current_count > (i+1)//2) & ((tot_count - current_count) > ((len(A) - (i+1))//2)):
            equi_leaders += 1
    
    return equi_leaders
    
  def goldenLeader_return_count(A):
    n = len(A)
    size = 0
    for k in xrange(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
    candidate = -1
    if (size > 0):
        candidate = value
    leader = -1
    count = 0
    for k in xrange(n):
        if (A[k] == candidate):
            count += 1
    if (count > n // 2):
        leader = candidate
    return leader, count
