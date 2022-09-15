class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [2, 3, -2, 4]
        # -n < 0 < n
        largestProduct = nums[0]
        maxProduct = 1
        minProduct = 1
        
        for n in nums:
            maxTemp = maxProduct
            maxProduct = max(n, maxProduct * n, minProduct * n)
            minProduct = min(n, maxTemp * n, minProduct * n)
            largestProduct = max(maxProduct, largestProduct)
        return largestProduct
            
        
        