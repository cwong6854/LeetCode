class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0
        index2 = len(numbers) - 1
        while index1 < index2:
            if numbers[index1] + numbers[index2] > target:
                index2 -=1
            elif numbers[index1] + numbers[index2] < target:
                index1 +=1
            elif numbers[index1] + numbers[index2] == target:
                return [index1+1,index2+1]
            else:
                continue

                
        
            # [0,0,0,2,3,9,9,9,9,]
        
        # index1 = 0
        # endpoint = len(numbers)
        # while index1 < endpoint:
        #     for index2 in range(index1, endpoint):
        #         if index1 == index2:
        #             continue
        #         if numbers[index1] + numbers[index2] == target:
        #             return [index1+1, index2+1]
        #     index1 +=1 
        
        # [2,7,11,15]
        