def solution(A):
    head=A[0]
    tail=sum(A[1:])
    tapes=[abs(head-tail)]
    for i in range(1,len(A)-1):
        head=head+A[i]
        tail=tail-A[i]
        tapes.append(abs(head-tail))
    return min(tapes)
    pass

print(solution([3,1,2,4,3]))
print(solution([3,1]))