class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        for i in nums:
            map[i] = map.get(i,0) + 1
        for k,v in map.items():
            if v == 1:
                return k