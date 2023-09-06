class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        # if n >= 5000:
        #     return 1
        # def solve(a,b):

        #     if a<=0 and b<=0:
        #         return 0.5
        #     if a<=0:
        #         return 1.0
        #     if b<=0:
        #         return 0.0
        #     return 0.25*(solve(a-100,b)+solve(a-75,b-25)+solve(a-50,b-50)+solve(a-25,b-75))
    
        # return solve(n,n)
        memo = {}
        
        def dfs(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if b <= 0:
                return 0
            if a <= 0:
                return 1

            if (a, b) in memo:
                return memo[(a, b)]

            prob_a1 = dfs(a - 100, b)
            prob_a2 = dfs(a - 75, b - 25)
            prob_a3 = dfs(a - 50, b - 50)
            prob_a4 = dfs(a - 25, b - 75)

            memo[(a, b)] = 0.25 * (prob_a1 + prob_a2 + prob_a3 + prob_a4)
            return memo[(a, b)]

        return 1 if n >= 4800 else dfs(n, n)