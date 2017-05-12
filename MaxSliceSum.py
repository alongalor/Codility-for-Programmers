def solution(A):
    max_ending = max_slice = -float('inf')
    for a in A:
        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice
