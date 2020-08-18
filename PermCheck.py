def solution(A):
    n=len(A)
    values=[False]*n
    for a in A:
        if a>n or values[a-1]:
            return 0
        else:
            values[a-1]=True
    return 1
    pass

print(solution([4,1,3,2]))
print(solution([4,1,3]))
print(solution([4,1,3,5]))
print(solution([1]))