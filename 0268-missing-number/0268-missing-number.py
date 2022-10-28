class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # first sort nums so that we can match index and value
        nums.sort()
        n = len(nums)
        for i, v in enumerate(nums):
            if i != v:
                return i
        return n
            