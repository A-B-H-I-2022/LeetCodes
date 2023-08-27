class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        answer,l = 0,0
        for r in range(len(nums)):
            if nums[r] == 0:
                if k == 0:
                    while nums[l] != 0:
                        l += 1
                    l +=1 
                else:
                    k -= 1
            answer = max(answer, r-l+1)
        return answer




        # answer = 0
        # zero = 0
        # b,i,j = 0,0,0
        # if k == 0:
        #     for i in nums:
        #         if i == 1:
        #             answer += 1
        #             b = max(answer , b)
        #         else:
        #             answer = 0
        #     return b
        # while j < len(nums):
        #     while i < len(nums):
        #         if nums[i] == 0:
        #             zero += 1
        #         if nums[i] == 1 or (nums[i] == 0 and zero <= k):
        #             answer += 1
        #             b = max(answer, b)
        #         else:
        #             answer = 1
        #             zero = 1
        #         i += 1
        #     i = j + 1
        #     j += 1
        #     answer = 0
        #     zero = 0
        # return b