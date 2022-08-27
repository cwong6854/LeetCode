class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        curSum = 0
        length = len(nums)
        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum = curSum + nums[i]
            maxSum = max(curSum, maxSum)
            print(curSum)
        return maxSum
        