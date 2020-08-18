def solution(A):
    n=len(A)
    if n==3:
        return A[0]*A[1]*A[2]
    if n==4:
        return max(A[0]*A[1]*A[2],A[0]*A[1]*A[3],A[0]*A[3]*A[2],A[3]*A[1]*A[2])
    else: #now we know there are at least five elements
        max1=max(A)
        A.remove(max1)
        max2=max(A)
        A.remove(max2)
        max3=max(A)
        A.remove(max3)
        min1=min(A)
        A.remove(min1)
        min2=min(A)
        A.remove(min2)
        print(max1,max2,max3)
        return max(max1*max2*max3,max1*min1*min2)
    pass

print(solution([1,2,3,3]))
print(solution([-1,-2,-3,-3]))
print(solution([-1,2,-3,-3]))
print(solution([-1,2,3,-3]))
print(solution([-4, -6, 3, 4, 5]))
print(solution([4, 7, 3, 2, 1, -3, -5]))