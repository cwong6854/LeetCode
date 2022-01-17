class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        count = length
        while count >= 0:
            if count in nums:
                count -= 1
            else:
                return count
        