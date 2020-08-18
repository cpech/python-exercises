def solution(S):
    n=len(S)
    if n==0:
        return 1
    open=0
    for i in range(n):
        if S[i]=='(':
            open+=1
        else:
            open-=1
            if open<0:
                return 0
    if open==0:
        return 1
    else:
        return 0
    pass

print(solution('(()(())())'))
print(solution('())'))
print(solution('(('))