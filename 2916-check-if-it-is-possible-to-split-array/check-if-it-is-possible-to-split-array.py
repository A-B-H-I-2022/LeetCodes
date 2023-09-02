class Solution(object):
    def canSplitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: bool
        """
        if len(nums) < 3:
            return True
        flag = 0
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] >= m:
                flag = 1
        if flag:
            return True
        else:
            return False


        # l = 0
        # flag = 1
        # r = len(nums)-1
        # if len(nums) <= 2:
        #     return True
        # while l < r:
        #     if sum(nums[l:r+1]) >= m:
        #         r -= 1
        #     else:
        #         r += 1
        #         l += 1
        #         if sum(nums[l:r+1]) < m:
        #             flag = 0
        #             break
        # if flag == 0:
        #     l = 0
        #     r = len(nums) - 1
        #     while l < r:
        #         if sum(nums[l:r+1]) >= m:
        #             l += 1
        #         else:
        #             r -= 1
        #             l -= 1
        #             if sum(nums[l:r+1]) < m:
        #                 flag = 0
        #                 break


        # if flag or l == r:
        #     return True
        # else:
        #     return False