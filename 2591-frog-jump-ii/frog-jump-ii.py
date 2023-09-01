class Solution(object):
    def maxJump(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        ans = stones[1] - stones[0]
        if len(stones) < 4:
            return stones[-1] - stones[0]
        else:
            for i in range(2,len(stones)):
                ans =  max(stones[i] - stones[i-2],ans)
        return ans

        