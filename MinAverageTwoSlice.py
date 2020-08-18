#should be O(n) complexity in time and space
def solution(A):
    n=len(A)
    current_average=(A[0]+A[1])/2
    average_of_two=(A[0]+A[1])/2
    average_from_start=(A[0]+A[1])/2
    start=0
    min_average=(A[0]+A[1])/2
    min_start=0
    for i in range(2,n):
        average_from_start=(((i-start)*current_average+A[i])/(i+1-start)) #average from start to i
        average_of_two=(A[i-1]+A[i])/2 #average of A[i-1] and A[i]
        if average_from_start>average_of_two:
            start=i-1
            current_average=average_of_two
        else:
            current_average=average_from_start
        if current_average<min_average: #update min_average if needed
            min_average=current_average
            min_start=start
    return min_start
    pass

#print(solution([4,2,2,5,1,5,8]))
#print(solution([7,6,5,4,3,2]))
#print(solution([2,3,4,5,6,7]))
#print(solution([7,-6,5,-4,3,-2]))
print(solution([-3,-5,-8,-4,-10]))
