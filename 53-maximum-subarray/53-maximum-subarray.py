class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # subarray could be [1]
        maxSum = nums[0]
        curSum = 0
        # [-2, 1] -> -1
        length = len(nums)
        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum = curSum + nums[i]
            maxSum = max(curSum, maxSum)
            print(curSum, maxSum)
        return maxSum
        