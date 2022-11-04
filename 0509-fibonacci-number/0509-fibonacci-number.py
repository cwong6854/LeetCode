class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n):
            if n == 0 or n == 1:
                return n
            return helper(n-1) + helper(n-2)
        return helper(n)
        