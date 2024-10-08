class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        dp = [True] * n
        dp[0] = dp[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if dp[i]:
                dp[i*i:n:i] = [False] * len(dp[i*i:n:i])

        return sum(dp)

        # count = 1
        # flag = 0
        # if n < 3:
        #     return 0
        # elif n >= 3:
        #     for i in range(3,n):
        #         for j in range(2,i):
        #             if i%j == 0:
        #                 flag = 1
        #         if not flag:
        #             count += 1
        #         flag = 0
        # return count

                        
        