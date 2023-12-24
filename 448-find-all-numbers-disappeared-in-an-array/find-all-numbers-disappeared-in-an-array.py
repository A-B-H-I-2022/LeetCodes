class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #TLE
        # ans = []
        # n = len(nums)
        # for i in range(n):
        #     ans.append(i+1)
        # for i in nums:
        #     if i in ans:
        #         ans.remove(i) 
        # return ans

        return set(range(1,len(nums)+1)) - set(nums)