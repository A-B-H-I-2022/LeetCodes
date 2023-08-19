class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        initial = nums[0]
        for i in range(1, len(nums)):
            if initial == 0:
                return False
            initial -= 1
            initial = max(initial, nums[i])
        return True


























        # current = nums[0]
        # for i in range(1,len(nums)):
        #     if current == 0:
        #         return False
        #     current -= 1
        #     current = max(current, nums[i])
        # return True
    