class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, longest = set(nums), 0
        for num in s:
		    if num - 1 in s:continue
		    j = 1
		    while num + j in s:j += 1
		    longest = max(longest, j)
        return longest
        # nums.sort()
        # print(nums)
        # a,c = 1,1
        # if len(nums) == 0:
        #     return 0
        # elif len(nums) == 1:
        #     return 1
        # else:
        #     for i in range(len(nums)-1):
        #         if (nums[i+1] - nums[i]) == 1:
        #             c += 1
        #             a = max(a,c)
        #         elif (nums[i+1] - nums[i]) == 0:
        #             continue
        #         else:
        #             c = 1                   
        #     return a