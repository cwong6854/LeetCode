class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # a + b = target
        # b = target - a
        # store indices inside a hashmap
        dic = {}
        for i in range(len(nums)):
            b = target - nums[i]
            if b not in dic:
                dic[nums[i]] = i
            else:
                return [i, dic[b]]