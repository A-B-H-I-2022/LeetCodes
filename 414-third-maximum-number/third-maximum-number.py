class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = sorted(list(set(nums)))
        if len(n) > 2:
            return n[-3]
        return n[-1]