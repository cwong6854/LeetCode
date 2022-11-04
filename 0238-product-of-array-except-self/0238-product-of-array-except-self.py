class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)
        prefix = 1
        for i in range(len(answer)):
            answer[i] *= prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(answer) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
            