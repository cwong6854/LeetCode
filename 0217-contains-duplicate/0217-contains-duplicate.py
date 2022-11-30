class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                return True
        return False
        