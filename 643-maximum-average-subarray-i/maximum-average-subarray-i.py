class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i = 0
        answer = sum(nums[i:i+k]) 
        temp = sum(nums[i:i+k])
        i=i+1
        l = len(nums)
        while i <= l-k:
            temp = temp - nums[i-1] + nums[i+k-1]
            answer = max(temp,answer)
            i += 1
        return answer / float(k)