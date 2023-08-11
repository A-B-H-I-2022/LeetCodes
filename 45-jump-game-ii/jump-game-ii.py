class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right,maxjump = 0,0,0
        answer = 0
        while right < len(nums)-1:
            for i in range(left , right + 1):
                maxjump = max(maxjump , i + nums[i])
            left = right + 1
            right = maxjump
            answer += 1
        return answer
