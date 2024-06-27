class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sq = [x**2 for x in range(1,int(sqrt(n))+1)]
        dp = [n]*(n+1)
        dp[0] = 0
        for target in range(1,n+1):
            for s in sq:
                if target-s >= 0:
                    dp[target] = min(dp[target], 1+dp[target-s])
        
        return dp[n]