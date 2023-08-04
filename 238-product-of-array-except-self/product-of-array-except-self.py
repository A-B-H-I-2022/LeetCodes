class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = [1 for i in range(len(nums))]
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            a[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            a[i] *= postfix
            postfix *= nums[i]
        return a