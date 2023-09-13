class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dp = [0]*len(arr)
        dp1 = [0]*len(arr)
        ans = 0
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                dp[i] = dp[i-1] + 1
        for j in range(len(arr)-2,-1,-1):
            if arr[j] > arr[j+1]:
                dp1[j] = dp1[j+1] + 1
        for i in range(len(arr)):
            if dp[i] > 0 and dp1[i] > 0:
                ans = max(ans,dp[i] + dp1[i] + 1)
        return ans

        

        # dp = [0] * len(arr)
        # for i in range(1, len(arr)):
        #     if arr[i] > arr[i-1]:
        #         dp[i] = dp[i-1] + 1
        # print(dp)
        # dp2 = [0] * len(arr)
        # for i in range(len(arr)-2, -1, -1):
        #     if arr[i] > arr[i+1]:
        #         dp2[i] = dp2[i+1] + 1
        # print(dp2)
        # res = 0
        # for i in range(len(arr)):
        #     if dp[i] > 0 and dp2[i] > 0:
        #         res = max(res, dp[i] + dp2[i] + 1)
        # return res