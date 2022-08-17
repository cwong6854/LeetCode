class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # at minimum -> O(n^2)
        # largestSum = []
        # numsLength = len(nums)
        # if numsLength == 1:
        #     return nums[0]
        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i, numsLength):
        #         total += nums[j]
        #         if len(largestSum) == 0:
        #             largestSum.append(total)
        #         else:
        #             if total > largestSum[0]:
        #                 largestSum[0] = total
        # return largestSum[0]

        largestSum = nums[0]
        curSum = 0
        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            largestSum = max(curSum, largestSum)
        return largestSum