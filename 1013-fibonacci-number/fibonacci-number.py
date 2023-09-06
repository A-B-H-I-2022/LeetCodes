class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp = [-1]*(n+1)
        # def fibonacci(n):
        #     if dp[n] != -1:
        #         return dp[n]
        #     dp[n] = dp[n-1] + dp[n-2]
        # return dp[n]
        # a,b,s = 0,0,0
    
        a,b,s = 0, 1, 0
        if n>1:
            for i in range(1,n):
                s = a+b
                a = b
                b = s 
            return s
        elif n == 1:
            return 1
        else:
            return 0