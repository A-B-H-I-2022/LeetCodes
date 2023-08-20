class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a,b = float('inf'),float('inf')
        for i in nums:
            if i <= a:
                a = i
            elif i <= b:
                b = i
            else: 
                return True
        return False
        # i = 0
        # l = len(nums)
        # while i < l-2:
        #     if nums[i]<nums[i+1] and nums[i+1]<nums[i+2]:
        #         return True
        #     i += 1
        # return False
