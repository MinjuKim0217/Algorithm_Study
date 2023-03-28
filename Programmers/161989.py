def solution(n, m, section):
    answer = 1
    current=section[0]
    
    for s in section:
        if current+m<=s:
            answer+=1
            current=s
    
    return answer
