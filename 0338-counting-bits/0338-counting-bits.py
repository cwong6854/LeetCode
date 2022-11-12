class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # runtime: o(nlogn)
        
        # res = []
        # for i in range(n+1):
        #     arr = []
        #     while i > 0:
        #         arr.append(i % 2)
        #         i = i // 2
        #     res.append(sum(arr))
        # return res
        
        dp = [0] * (n+1)
        x = 1
        # loop through each index until n
        for i in range(1, n + 1):
            if x * 2 == i:
                x = x*2
            dp[i] = 1 + dp[i-x]
        return dp
        
        
    
            
        
        