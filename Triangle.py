def solution(A):
    n=len(A)
    if n<3:
        return 0
    A.sort(reverse=True)
    i=0
    while i<n-2:
        if A[i]<A[i+1]+A[i+2]:
            return 1
        i+=1
    return 0
    pass

print(solution([10,2,5,1,8,20]))
print(solution([10,50,5,1]))