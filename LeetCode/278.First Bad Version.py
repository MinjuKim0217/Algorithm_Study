# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
    
        index= n//2
        l= 0
        r= n-1
        lowest = n
        while(l<=r):
            if(isBadVersion(index)):
                lowest = index
                r = index-1
                index = (l+r)//2
                
            else:
               
                l=index+1
                index = (l+r)//2
        
        return lowest
