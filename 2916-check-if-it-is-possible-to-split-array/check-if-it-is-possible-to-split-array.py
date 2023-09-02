class Solution(object):
    def canSplitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: bool
        """
        if len(nums) < 3:
            return True
        flag = 0
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] >= m:
                return True
        return False