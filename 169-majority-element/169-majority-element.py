class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        n = 0
        total = 0
        numbers = set(nums)
        for i in numbers:
            count = 0
            for j in range(len(nums)):
                if nums[j] == i:
                    count += 1
            if count > total:
                total = count
                n = i
            else:
                count = 0
        return n