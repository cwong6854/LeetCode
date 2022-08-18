class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
            
            
    #         largestProduct -> the number itself
    #         case with all positives: the whole array itself
    #         case with negatives: 
    #         case with 0 in the array: could cause the rest of products to become 0
    #         need to store the previous maximum number, would also need to store the minimum number, to compare with max

    #         PV -> -x < 0 < x
    
        largestProduct = nums[0]
        maxProduct = 1
        minProduct = 1
        
        # 1 * 2 = 2 -> maxProduct = 2, minProduct = 2
        # 2 * 3 = 6 -> maxProduct = 6, minProduct = 2
        # 6 * -2 = 12 -> maxProduct = 6, minProduct = -12
        # 6 * 4 = 24 -> error
        
        for n in nums:
            maxTemp = maxProduct
            maxProduct = max(n, maxProduct * n, minProduct * n)
            minProduct = min(n, maxTemp * n, minProduct * n)
            largestProduct = max(maxProduct, largestProduct)
        return largestProduct
        