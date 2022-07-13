class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        
        else:
            i=0
            for j in nums:
                if j<target:
                    i+=1
                else:
                    break
                    
            return i
