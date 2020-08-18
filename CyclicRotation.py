def rotate_once(A):
    if A!=[]:
        A.insert(0,A.pop(-1))
    return A
    pass

def solution(A,K):
    if A!=[]:
        i=K%len(A)
        while i>0:
            rotate_once(A)
            i-=1
    return A
    pass

print(solution([1,2,3,4],5))