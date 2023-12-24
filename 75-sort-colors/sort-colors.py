class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i,l,r = 0,0,len(nums)-1
        def swap(a,b):
            temp = nums[b]
            nums[b] = nums[a]
            nums[a] = temp
        while i <= r:
            if nums[i] == 0:
                swap(l,i)
                l += 1
            elif nums[i] == 2:
                swap(i,r)
                r -= 1
                i -= 1
            i += 1
        return nums