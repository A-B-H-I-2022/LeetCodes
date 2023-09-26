class Solution(object):
    def maximumSumOfHeights(self, maxHeights):
        """
        :type maxHeights: List[int]
        :rtype: int
        """
        res = 0
        n = len(maxHeights)
        for i in range(n):
            cur = v = maxHeights[i]
            for j in range(i - 1, -1, -1):
                v = min(v, maxHeights[j])
                cur += v
            v = maxHeights[i]
            for j in range(i + 1, n):
                v = min(v, maxHeights[j])
                cur += v
            res = max(res, cur)
        return res