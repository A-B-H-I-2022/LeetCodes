class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        current = nums[0]
        for i in range(1,len(nums)):
            if current == 0:
                return False
            current -= 1
            current = max(current, nums[i])
        return True
        # left,right,jump = 0,0,0
        # l = len(nums)
        # while right <= l - 1:
        #     for i in range(left,right+1):
        #         jump = max(jump,i + nums[i])
        #     left = right + 1
        #     right = jump
        #     if right == l-1:
        #         return True
        # return False
