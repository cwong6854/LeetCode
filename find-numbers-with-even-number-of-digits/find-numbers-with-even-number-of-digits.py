class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        total = 0
        for n in nums:
            for digit in str(n):
                count += 1
            if count % 2 == 0:
                total += 1
            else:
                count = 0
        return total
            
            
        