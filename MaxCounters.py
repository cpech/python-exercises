#correct O(n*m) algorithm
def solution2(N,A):
    is_max=[True]*N #records whether counter is maximal
    max_value=0 #records maximal counter value
    counters=[0]*N #list of counters
    for a in A:
        if a==N+1: #if the operation is max counter
            if all(is_max): #if all counters are maximal
                max_value+=1 #max_value is increased
                counters=[max_value]*N #all counters are set to max_value
            else:
                counters=[max_value]*N #all counters are set to max_value
                is_max=[True]*N #all counters are now maximal
        else: #if the operation isn't max counter but increase counter a-1
            counters[a-1]+=1 #increase counter a-1
            if is_max[a-1]: #if counter to increase was maximal
                max_value+=1 #increase max_value
                is_max=[False]*N 
                is_max[a-1]=True #only maximal counter is now a-1
            elif counters[a-1]==max_value: #if counter a-1 becomes maximal after increase
                is_max[a-1]=True #counter a-1 becomes maximal
    return counters
    pass

#optimal algorithm
def solution(N,A):
    min_value=0 #records minimal counter value
    max_value=0 #records maximal counter value
    counter=[0]*N #list of counters
    for a in A:
        if a==N+1: #if the operation is max counter
            min_value=max_value #new minimal value is max_value
        else: #if the operation is not max counter
            if counter[a-1]<min_value: #counter to be increased has not been updated
                counter[a-1]=min_value #update counter
            counter[a-1]+=1 #increase counter
            if counter[a-1]>max_value: #if increased counter is larger than max_value
                max_value=counter[a-1] #update max_value
    for i in range(N):
        if counter[i]<min_value:
            counter[i]=min_value #final counters update
    return counter
    pass

print(solution(5,[3,4,4,6,1,4,4]),solution2(5,[3,4,4,6,1,4,4]))