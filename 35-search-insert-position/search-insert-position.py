class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1 
        while left <= right:
            flag = 0
            mid =  (left + right) // 2
            if nums[mid] == target:
                return mid
                flag = 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if not flag:
            if nums[mid] > target:
                return mid
            else:
                return mid + 1