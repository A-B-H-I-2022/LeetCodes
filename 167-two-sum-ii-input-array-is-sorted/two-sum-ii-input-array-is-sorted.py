class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for k,v in enumerate(numbers):
            d = target - v
            if d in map:
                return [map[d]+1,k+1]
            map[v] = k