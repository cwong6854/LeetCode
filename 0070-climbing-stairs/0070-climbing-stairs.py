class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # one, two = 1, 2
        # all_ways = 0
        # # 1 <= n <= 45
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # for i in range(3, n+1):
        #     all_ways = one + two
        #     one = two
        #     two = all_ways
        # return all_ways
        one, two = 1, 1
        for i in range(n):
            one, two = one + two, one
        return two
            