class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        # at n >= 3 --> want to store our steps and track all distinct ways
        one = 1
        two = 2
        all_ways = 0
        for i in range(3, n+1):
            all_ways = one + two
            one = two
            two = all_ways
        return all_ways
            