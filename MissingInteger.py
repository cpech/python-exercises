def solution(A): #the missing integer must be between 1 and len(A)+1
    n=len(A) 
    seen=[False]*(n+1) #records if integer was seen
    for a in A:
        if 1<=a<=n+1:
            seen[a-1]=True
    i=0
    while i<n+1:
        if not seen[i]:
            return i+1 #returns first missing integer
        i+=1
    pass

print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2,3]))
print(solution([-1,- 3]))