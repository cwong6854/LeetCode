class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lst = []
        if len(nums1) < len(nums2):
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    lst.append(nums1[i])
        else:
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    lst.append(nums2[i])
                    
                    
        return set(lst)