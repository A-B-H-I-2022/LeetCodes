class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """

        maxSum = 0
        i, j = 0, 0
        max1, max2 = 0, 0
        while i < len(nums) - firstLen + 1:
            max1 = sum(nums[i:i + firstLen])
            if secondLen <= i:
                j = 0
                while j + secondLen <= i:
                    max2 = sum(nums[j:j + secondLen])
                    maxSum = max(maxSum, max1 + max2)
                    j += 1

            if len(nums) - (i + 1) >= secondLen:
                j = 0
                while j + i + secondLen <= len(nums):
                    max2 = sum(nums[i + j + firstLen:i + j + firstLen + secondLen])
                    maxSum = max(maxSum, max1 + max2)
                    j += 1
            i += 1
        return maxSum