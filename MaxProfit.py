def solution(A):
    B = []
    for i in range(len(A) - 1):
        B.append(A[i+1] - A[i])

    max_ending = max_slice = 0
    for i in B:
        max_ending = max(0, max_ending + i)
        max_slice = max(max_slice, max_ending)
    return max_slice
