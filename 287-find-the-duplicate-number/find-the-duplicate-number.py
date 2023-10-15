class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                x = i
                break
        return x
        