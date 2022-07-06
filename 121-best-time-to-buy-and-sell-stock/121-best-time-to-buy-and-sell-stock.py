class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        left = 0
        right = 1
        while right < len(prices):
            difference = prices[right] - prices[left]
            if prices[left] < prices[right]:
                profit = max(profit, difference)
            else:
                left = right
            right += 1
        return profit
            