def solution(A):
    values=dict()
    for a in A:
        values[a]=values.get(a,0)+1
    return len(values)
    pass

print(solution([2,1,1,2,3,1]))