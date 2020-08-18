import math

def solution(A,B,K):
    return math.floor(B/K)+1-math.ceil(A/K)
    pass

print(solution(6,11,2))
print(solution(7,11,2))
print(solution(6,11,3))
print(solution(6,12,3))
print(solution(5,12,3))