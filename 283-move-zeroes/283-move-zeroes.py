class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        count2 = 0
        for i in nums:
            if i == 0:
                nums.append(0)
                nums.remove(0)
        
                