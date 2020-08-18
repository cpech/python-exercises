#expected worst-case time complexity is O(N+M); expected worst-case space complexity is O(N), 
# beyond input storage (not counting the storage required for input arguments). Elements of input 
# arrays can be modified.

def solution(S, P, Q):
    n=len(S)
    count = [[0]*(n+1),[0]*(n+1),[0]*(n+1)]
    result = []
    m=len(P)
    for i in range(n):
        if S[i]=='A':
            count[0][i+1] = count[0][i] + 1
        elif S[i]=='C':
            count[0][i+1] = count[0][i]
            count[1][i+1] = count[1][i] + 1
        elif S[i]=='G':
            count[0][i+1] = count[0][i]
            count[1][i+1] = count[1][i]
            count[2][i+1] = count[2][i] + 1
        else:
            count[0][i+1] = count[0][i]
            count[1][i+1] = count[1][i]
            count[2][i+1] = count[2][i]
    for i in range(m):
      start = P[i]
      end = Q[i]+1
      if count[0][end] - count[0][start]:
          result.append(1)
      elif count[1][end] - count[1][start]:
          result.append(2)
      elif count[2][end] - count[2][start]:
          result.append(3)
      else:
          result.append(4)
    return result
    pass

print(solution('CAGCCTA',[2,5,0],[4,5,6]))
print(solution('CCCCCCCC',[2,5,0],[4,5,6]))
print(solution('AC', [0, 0, 1], [0, 1, 1]))