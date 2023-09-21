class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        map = {}
        lis = []
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
        print(map)
        for k,v in map.items():
            if v == 2:
                lis.append(k)
        return lis
        