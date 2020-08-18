def solution(X, Y, D):
    quotient=(Y-X)//D
    remainder=(Y-X)%D
    if remainder==0:
        return quotient
    else:
        return quotient+1
    pass

print(solution(10,85,30))
print(solution(10,100,30))