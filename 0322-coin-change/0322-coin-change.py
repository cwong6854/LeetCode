class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # DFS -> Bottom Up Dynamic Programming
        # dp -> array of amounts -> solving subproblems to solve larger problems
        dp = [amount+1] * (amount + 1)
        # at 0 amount, we need only 0 coins
        dp[0] = 0
        # for each a -> amounts, if amount - coin is non-negative, then we store amount into our dp array, and take the minimum between dp[a] and 1 + dp[a-c]
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[amount] if dp[amount] != amount+1 else -1