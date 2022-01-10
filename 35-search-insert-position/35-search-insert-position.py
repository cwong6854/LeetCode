class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        else:
            for i in range(len(nums)):
                if nums[len(nums) - 1] < target:
                    return len(nums)
                elif nums[i] > target:
                    return 0
                else:
                    if nums[i] < target and nums[i + 1] > target:
                        return i + 1