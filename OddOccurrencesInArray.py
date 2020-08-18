def solution(A):
    values=dict()
    for a in A:
        values[a]=values.get(a,0)+1
    for a in values:
        if values[a]%2==1:
            return a
    pass

print(solution([9,3,9,9,3,9,9,7,9]))