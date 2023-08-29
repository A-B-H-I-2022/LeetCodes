class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        if r == 0:
            return 0
        while l < r:
            mid = l + (r-l)//2
            if nums[mid]<nums[mid+1]:
                l = mid+1
            else:
                r = mid
        return l