def solution(absolutes, signs):
    answer=0;
    length=len(absolutes)
    for i in range (0, length):
        if signs[i]:
            answer+=absolutes[i]
            
        else:
            answer-=absolutes[i]
    return answer
