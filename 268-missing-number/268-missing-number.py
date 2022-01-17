class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        n = length
        for i in range(length):
            if i not in nums:
                n = i
            else:
                continue
        return n
        