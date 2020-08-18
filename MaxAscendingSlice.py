def solution(A):
    max_slice_start=0
    max_slice_size=1
    current_slice_size=1
    current_slice_start=0
    n=len(A)
    for i in range(1,n):
        if A[i]>A[i-1]: #if current slice continues to grow
            current_slice_size+=1
        else: #current slice ends
            if current_slice_size>max_slice_size: #if the now ended current slice is longer than the previous max
                max_slice_size=current_slice_size #update max slice
                max_slice_start=current_slice_start
            current_slice_start=i #start new slice at i
            current_slice_size=1 #it has size 1
    if current_slice_size>max_slice_size: #if current_slice wasn't ended at n and is now bigger
        return current_slice_start
    else:
        return max_slice_start
    pass

print(solution([2,2,2,2,1,2,-1,2,1,3]))
print(solution([2,2,2,2,1,2,-1,2,1,3,4]))