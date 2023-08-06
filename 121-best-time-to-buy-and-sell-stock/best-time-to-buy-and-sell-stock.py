class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return profit

     


        # p = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         p = max(p , prices[j] - prices[i])
        # if p == 0:
        #     return 0
        # else:
        #     return p