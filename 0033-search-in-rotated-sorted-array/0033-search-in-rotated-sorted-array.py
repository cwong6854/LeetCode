class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            midpoint = (l + r) // 2

            if nums[midpoint] == target:
                return midpoint

            if nums[midpoint] > target:
                if nums[l] <= target <= nums[midpoint]:
                    r -= 1
                else:
                    l += 1
            if nums[midpoint] < target:
                if nums[midpoint] <= target <= nums[r]:
                    l += 1
                else:
                    r -= 1
        return -1
        