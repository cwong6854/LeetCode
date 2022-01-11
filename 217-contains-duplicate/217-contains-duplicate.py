class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # sets cannot have duplicates
        # if item exists in the set, cannot be added -> return True
        # otherwise, return False
        sets = set()
        for i in nums:
            if i not in sets:
                sets.add(i)
            else:
                return True
        return False
        # another faster runtime solution
        # return (len(nums)) != (len(set(nums)))