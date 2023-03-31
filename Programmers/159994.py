def solution(cards1, cards2, goal):
    
    i,j=0,0
    
    len_card1, len_card2= len(cards1), len(cards2)
    
    for word in goal:
        if i<len_card1 and word==cards1[i]:
            i+=1
        elif j<len_card2 and word==cards2[j]:
            j+=1
        else:
            return 'No'
        
    return 'Yes'
        
