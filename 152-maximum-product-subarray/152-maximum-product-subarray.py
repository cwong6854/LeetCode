class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [2, 3, -2, 4]
        # -n < 0 < n
        
        #edge cases
        # all positives -> whole array itself
        # negatives -> don't want to return a big negative value -> keep track of min value
        # 0: can bring the rest of our products to 0
        
        largestProduct = nums[0]
        maxProduct = 1
        minProduct = 1
        
        for n in nums:
            maxTemp = maxProduct
            maxProduct = max(n, maxProduct * n, minProduct * n)
            minProduct = min(n, maxTemp * n, minProduct * n)
            largestProduct = max(largestProduct, maxProduct)
            print(largestProduct, maxProduct, minProduct)
        return largestProduct
            
        
        