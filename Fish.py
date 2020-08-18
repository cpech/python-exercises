def solution(A,B):
    n=len(A)
    alive=n #number of fish currently alive
    current_down_fishes=[]
    for i in range(n):
        if B[i]==1: #add fish i to downstream fishes
            current_down_fishes.append(i)
        else:
            while current_down_fishes!=[]: #while there are still downstream fishes left
                if A[current_down_fishes[-1]]<A[i]: #if the upstream fish is bigger
                    #print('downstream fish ',current_down_fishes[-1],' is eaten')
                    alive-=1 
                    current_down_fishes.pop(-1) #the downstream fish is eaten
                else:
                    alive-=1 #the upstream fish is eaten
                    #print('upstream fish ',i,' is eaten')
    return alive
    pass

#print(solution([4,3,2,1,5],[0,1,0,0,0]))
#print(solution([4,3,2,1,5,6],[0,1,0,0,1,0]))
print(solution([4,3,2,1,5,6],[0,1,1,1,1,0]))
