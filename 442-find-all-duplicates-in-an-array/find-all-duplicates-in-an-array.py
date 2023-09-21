class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        map = {}
        ans = []

        for i in nums:
            if i in map:
                ans.append(i)
                del map[i]
            else:
                map[i] = 0
        return(ans)
       