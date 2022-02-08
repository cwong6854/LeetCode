class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        while zeros > 0:
            nums.append(0)
            nums.remove(0)
            zeros -= 1
        
                