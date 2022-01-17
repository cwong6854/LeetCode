class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            if i in nums and length in nums:
                continue
            elif length not in nums:
                return length
            else:
                return i
        