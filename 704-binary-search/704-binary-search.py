class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        # if target at middle index, return
        # if middle index less than target, search through right
        # else, search through left
        middle = length // 2
        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            for i in range(middle + 1, length):
                if nums[i] == target:
                    return i
        if nums[middle] > target:
            for i in range(middle - 1, -1, -1):
                if nums[i] == target:
                    print(i)
                    return i
        return -1
        