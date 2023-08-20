class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i,l = 0,len(nums)
        for j in range(l):
            if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1