class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        map = {}
        answer = 0
        for i in nums:
            if k-i in map and map[k-i]>0:
                answer += 1
                map[k-i] -= 1
            elif i not in map:
                map[i] = 1
            else:
                map[i] += 1
        return answer
        # nums.sort()
        # answer,left,right = 0,0,len(nums)-1
        # while left < right:
        #     summ = nums[left] + nums[right]
        #     if summ > k:
        #         right -= 1
        #     elif summ < k:
        #         left += 1
        #     else:
        #         answer += 1
        #         left += 1
        #         right -= 1
        # return answer