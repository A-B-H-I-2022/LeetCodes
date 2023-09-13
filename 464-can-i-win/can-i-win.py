class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        values = list(range(1,maxChoosableInteger+1))
        if desiredTotal <= 0:
            return True
        if sum(values)< desiredTotal:
            return False
        
        memo = {}

        def dp(values,total):
            if values[-1] >= total:
                return True
            if values in memo:
                return memo[values]

            for i in range(len(values)):
                if not dp(values[:i]+values[i+1:],total-values[i]):
                    memo[values] = True
                    return True
            memo[values] = False
            return False
        
        return dp(tuple(values),desiredTotal)      