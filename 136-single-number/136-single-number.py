class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        else:
            for i in set(nums):
                counts = nums.count(i)
                if counts == 1:
                    return i
                    