def solution(n):
    i=0
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=i 
        else:
            continue
    return cnt
