class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # runtime => O(N^2)
        # answer = []
        # index = 0
        # total = 1
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             total *= nums[j]
        #     answer.append(total)
        #     total = 1
        # return answer
        
#         nums_length = len(nums)
#         productExceptSelf = [1] * nums_length  
#         # prefix -> multiplying elements from the left
#         for i in range(1, nums_length):
#             productExceptSelf[i] = productExceptSelf[i - 1] * nums[i - 1]
#         # suffix - multiplying elements from the right
#         # since most right element has no right element, right starts at value of 1
#         right = 1
#         for i in range(nums_length - 1, -1, -1):
#             productExceptSelf[i] = productExceptSelf[i] * right
#             right = right * nums[i]

#         return productExceptSelf
            

        
        
        
        
        
        
        
        
        
        
        arr = [1] * len(nums)
        length = len(nums)
        prefix = 1
        for i in range(1, length):
            arr[i] = nums[i - 1] * arr[i - 1]
            prefix = nums[i - 1]
        right = 1
        for i in range(length - 1, -1, -1):
            arr[i] = right * arr[i]
            right *= nums[i]
        return arr
        
        
        
        
        
        
        
        
        
        
        

            
            
        