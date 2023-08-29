class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer,ans = 0,0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                answer += 1
                ans = max(answer, ans)
            else:
                answer = 0
        return ans+1