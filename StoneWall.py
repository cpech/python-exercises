def solution(H):
    n=len(H)
    nb_blocks=0
    current_walls=[]
    for height in H:
        while len(current_walls)!=0 and height<current_walls[-1]: 
            del current_walls[-1]
        if len(current_walls)!=0 and height==current_walls[-1]: #wall already counted
            pass
        else:
            nb_blocks+=1
            current_walls.append(height)
    return nb_blocks
    pass

print(solution([8,8,5,7,9,8,7,4,8]))