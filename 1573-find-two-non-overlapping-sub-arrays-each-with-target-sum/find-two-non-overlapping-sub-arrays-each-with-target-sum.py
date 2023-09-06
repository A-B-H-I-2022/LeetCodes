class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        dp = [float('inf')]*n
        left = 0
        answer = float('inf')
        summ = 0
        for right in range(n):
            summ += arr[right]
            while summ > target:
                summ -= arr[left]
                left += 1
            if summ == target:
                dp[right] = right - left + 1
                if left:
                    answer = min(answer, (dp[left-1] + right-left+1))
            dp[right] = min(dp[right-1],dp[right])
        return answer if answer != float('inf') else -1


        