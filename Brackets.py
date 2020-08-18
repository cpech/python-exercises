def solution(S):
    n=len(S)
    if n==0:
        return 1
    open_brackets=[]
    for i in range(n):
        if S[i]=='(' or S[i]=='[' or S[i]=='{':
            open_brackets.append(S[i])
        elif open_brackets==[]:
            return 0
        elif S[i]==')' and open_brackets[-1]!='(':
            return 0
        elif S[i]==']' and open_brackets[-1]!='[':
            return 0
        elif S[i]=='}' and open_brackets[-1]!='{':
            return 0
        else:
            del open_brackets[-1]
    if open_brackets==[]:
        return 1
    else:
        return 0
    pass

print(solution("{[()()]}"))
print(solution("([)()]"))