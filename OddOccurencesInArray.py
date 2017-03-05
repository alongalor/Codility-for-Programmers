def solution(A):
    d = {}
    for i in A:
        d[i] = d.get(i, 0) + 1

    spec_val = 0
    for i in d.values():
        if i%2 != 0:
            spec_val = i
            
    for key, val in list(d.iteritems()):
        if val == spec_val:
            return key