class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        dict={
            '(':')',
            '[':']',
            '{':'}'
        }
        
        stack=[]
        
        for i in s:
            if i in dict:
                stack.append(i)
            elif len(stack)==0 or dict[stack.pop()]!=i:
                return False
        return len(stack) ==0
