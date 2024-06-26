class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[-1]*n for _ in range(m)]
        def unique(i,j):
            if i == m-1 or j == n-1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = unique(i+1,j) + unique(i,j+1)
            return dp[i][j]
        return unique(0,0)

        