class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
                print(i)
            else:
                if abs(dic[nums[i]] - i) <= k:
                    return True
                else:
                    dic[nums[i]] = i
        return False