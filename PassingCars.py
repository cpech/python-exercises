def solution(A):
    nb_zeros=0 #number of zeros to current position
    passing_cars=0 #number of passing cars
    for a in A:
        if a==0: #if zero, increment nb_zeros
            nb_zeros+=1
        else: #if one, it passes all previous zeros
            passing_cars+=nb_zeros
            if passing_cars>1000000000:
                return -1
    return passing_cars
    pass

print(solution([0,1,0,1,1]))
