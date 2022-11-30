class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largestProduct = nums[0]
        maxProduct = 1
        minProduct = 1
        
        for n in nums:
            tmpProduct = maxProduct
            maxProduct = max(n, maxProduct * n, minProduct * n)
            minProduct = min(n, tmpProduct * n, minProduct * n)
            largestProduct = max(largestProduct, maxProduct)
        return largestProduct
            