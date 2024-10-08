class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        # """
        # left = 0
        # right = len(nums) - 1 
        # while left <= right:
        #     flag = 0
        #     mid =  (left + right) // 2
        #     if nums[mid] == target:
        #         return mid
        #         flag = 1
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     elif nums[mid] < target:
        #         left = mid + 1
        # if not flag:
        #     if nums[mid] > target:
        #         return mid
        #     else:
        #         return mid + 1

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return high + 1