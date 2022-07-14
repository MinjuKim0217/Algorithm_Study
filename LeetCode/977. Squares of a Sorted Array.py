class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new=[]
        for i in nums:
            if i<=0:
                new.append(i*(-1))
            else:
                new.append(i)
                
        new.sort()
        
        final=[]
        for i in new:
            square=i*i
            final.append(square)
            
        return final
