class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # [1,1,0,1,1,1]
        count = 0
        maxCount = 0
        for n in nums:
            if n == 0:
                if maxCount < count:
                    maxCount = count
                count = 0
            if n == 1:
                count += 1
        if count > maxCount:
            maxCount = count
        return maxCount
                
                
            
        