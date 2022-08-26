class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # p = 0
        # for i in range(len(prices)):
        #     for j in range(len(prices)):
        #         if j <= i: 
        #             continue
        #         else:
        #             profit = prices[j]
        #             if prices[i] < profit:
        #                 p = max(p, profit - prices[i])
        # return p
        
        p = prices[0]
        profit = 0
        for i in range(len(prices)):
            if i == 0:
                continue
            else:
                if prices[i - 1] < prices[i]:
                    profit = max(profit, prices[i] - prices[i - 1], prices[i] - p)
                if p > prices[i]:
                    p = prices[i]
        return profit
        # O(N^2)