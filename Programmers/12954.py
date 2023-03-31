def solution(x, n):
    answer = []
    i=0
    for i in range (1,n+1):
        add=x*i
        answer.append(add)
    return answer
