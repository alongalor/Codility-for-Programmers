def solution(S):
    A = ['']
    for i in xrange(len(S)):
        A += [S[i]]
        if A[-2:] in [["{","}"], ["[","]"], ["(",")"]]:
            A = A[:-2]
    if len(A)==1:
        return 1
    return 0