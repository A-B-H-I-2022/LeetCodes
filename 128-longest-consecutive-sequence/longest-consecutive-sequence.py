class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        c = 1
        a = 1
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        # elif len(nums) == 2 and (nums[0] == 0 and nums[1] == 0):
        #     return 1

        else:
            for i in range(len(nums)-1):
                if (nums[i+1] - nums[i]) == 1:
                    c += 1
                    a = max(a,c)
                elif (nums[i+1] - nums[i]) == 0:
                    continue
                else:
                    c = 1                   
            return a