def solution(A):
    n=len(A)
    return (n+1)*(n+2)//2-sum(A)
    pass

print(solution([2,3,1,5]))