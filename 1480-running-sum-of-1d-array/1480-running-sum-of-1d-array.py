class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 0
        output = []
        for i in nums:
            total += i
            output.append(total)
        return output