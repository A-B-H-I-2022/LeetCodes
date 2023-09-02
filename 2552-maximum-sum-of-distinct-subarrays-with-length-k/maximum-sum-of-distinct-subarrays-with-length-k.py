class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = collections.Counter()
        ans,l = 0,0
        res = 0
        n = len(nums)
        for i in range(n):
            ans += nums[i]
            if count[nums[i]] == 0:
                l += 1
            count[nums[i]] += 1
            if i >= k:
                ans -= nums[i-k]
                count[nums[i-k]] -= 1
                if count[nums[i-k]] == 0:
                    l -= 1
            if i >= k-1:
                if l == k:
                    res = max(res, ans)
        return res