def solution(X,A):
    n=len(A)
    leaves=[False]*X
    i=0
    while not all(leaves) and i<n:
        leaves[A[i]-1]=True
        i+=1
    if all(leaves):
        return i-1
    else:
        return -1
    pass

print(solution(5,[1,3,1,4,2,3,5,4]))
print(solution(5,[1,3,1,4,2,3,4]))
print(solution(5,[]))
print(solution(1,[1]))
print(solution(2,[1,2]))