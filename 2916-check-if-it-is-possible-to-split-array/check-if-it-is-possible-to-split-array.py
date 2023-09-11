class Solution(object):
    def canSplitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: bool
        """
        # if len(nums) < 3:
        #     return True
        # for i in range(len(nums)-1):
        #     if nums[i] + nums[i+1] >= m:
        #         return True
        # return False

        if len(nums) <= 2:
            return True
        
        for i in range(1, len(nums)):
            if nums[i] + nums[i-1] >= m:
                return True
        return False
            