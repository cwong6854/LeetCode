class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n = 1, then only one possible way
        if n == 1:
            return 1
        # if n = 2, then there's two possible ways
        if n == 2:
            return 2
        
        all_ways = 0
        one_step = 1
        two_step = 2
        
        for i in range(2, n):
            all_ways = one_step + two_step
            one_step = two_step
            two_step = all_ways
        return all_ways