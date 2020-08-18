def solution(N):
    binary=format(N,'b') #convert into binary
    return len(max(binary.strip('0').split('1'))) #remove trailing zeros, split at ones, return max gap
    pass
