class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # numb = set(nums)
        # count = 0
        # currnumb = 0
        # for i in numb:
        #     if count == 1:
        #         return currnumb
        #     else:
        #         count = 0
        #         currnumb = i
        #         for j in nums:
        #             if i == j:
        #                 count += 1
        # if count == 1:
        #     return currnumb
        if len(nums) == 1:
            return nums[0]
        else:
            for i in set(nums):
                counts = nums.count(i)
                if counts == 1:
                    return i
                    