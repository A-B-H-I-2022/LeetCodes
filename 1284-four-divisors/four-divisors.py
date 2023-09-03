class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            sol = set()
            for j in range(1, int(floor(sqrt(i))+1)):
                if i%j == 0:
                    sol.add(i // j)
                    sol.add(j)
                if len(sol) > 4:
                    break
            if len(sol) == 4:
                ans += sum(sol)
        return ans
