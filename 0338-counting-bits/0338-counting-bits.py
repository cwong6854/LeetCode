class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n+1):
            arr = []
            while i > 0:
                arr.append(i % 2)
                i = i // 2
            res.append(sum(arr))
        return res
    
            
        
        