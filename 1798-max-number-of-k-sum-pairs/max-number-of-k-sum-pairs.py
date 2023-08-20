class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        answer,left,right = 0,0,len(nums)-1
        while left < right:
            summ = nums[left] + nums[right]
            if summ > k:
                right -= 1
            elif summ < k:
                left += 1
            else:
                answer += 1
                left += 1
                right -= 1
        return answer