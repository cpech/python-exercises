def solution(A):
    values=dict()
    for a in A:
        values[a]=values.get(a,0)+1 #increases value of key a, or creates it if a wasn't in the dictionary
    count=0 #initialise count of pairs
    for v in values:
        count_v=values[v]
        count+=count_v*(count_v-1)//2 #add the binomial coefficient counting the number of pairs (=0 if count_v=1, 1 if count_v=2, etc)
    return count
    pass

print(solution([3,5,6,3,3,5]))