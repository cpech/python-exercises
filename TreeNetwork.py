def solution(T):
    n=len(T)
    adjacent_nodes=[[] for _ in range(n)]
    root=-1
    #next loop finds the root and creates adjacency lists
    for i in range(n): 
        if T[i]==i:
            root=i
        else:
            adjacent_nodes[i].append(T[i])
            adjacent_nodes[T[i]].append(i)
    #now prepare for breadth first search of the tree
    dist_to_root=[0]*n #dist_to_root[i] will store the distance of node i to root
    seen=[False]*n #seen[i] says whether node i has been seen by search
    queue=[root] #start exploring from the root
    seen[root]=True
    parent=[root]*n #will store the immediate ancestor of each node
    while len(queue)!=0:
        node=queue.pop(0) #remove first node from queue
        seen[node]=True #node is now seen
        if node!=root:
            dist_to_root[node]=dist_to_root[parent[node]]+1 #if the node is not the root compute its distance to root
        for adj in adjacent_nodes[node]: #now move to adjacent nodes
            if not seen[adj]:
                seen[adj]=True #now it was seen
                parent[adj]=node #its parent is node
                queue.append(adj) #add it to queue
    #now turn dist_to_root into the required output
    result=[0]*(n-1)
    for dist in dist_to_root:
        if dist!=0: #remove the root
            result[dist-1]+=1
    return result
    pass

print(solution([9,1,4,9,0,4,8,9,0,1]))

