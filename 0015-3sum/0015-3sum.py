class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # [-1,0,1,5,-1,-4]
        #  ^^            ^ 
        # three pointers -> i,j and k
        triplets = []
        sort_nums = sorted(nums)
        
        for i in range(len(sort_nums)):
            if i > 0 and sort_nums[i] == sort_nums[i - 1]:
                continue
            
            l, r = i+1, len(sort_nums) - 1
            while l < r:
                if sort_nums[i] + sort_nums[l] + sort_nums[r] > 0:
                    r -= 1
                elif sort_nums[i] + sort_nums[l] + sort_nums[r] < 0:
                    l += 1
                else:
                    triplets.append([sort_nums[i], sort_nums[l], sort_nums[r]])
                    l += 1
                    while sort_nums[l] == sort_nums[l - 1] and l < r:
                        l += 1
        return triplets
                    