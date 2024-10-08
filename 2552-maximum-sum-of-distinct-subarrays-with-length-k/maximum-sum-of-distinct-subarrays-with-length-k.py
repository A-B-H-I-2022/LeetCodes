class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_sum = 0
        current_sum = 0
        left,right = 0,0
        taken = set()
        while right < len(nums):
            if nums[right] not in taken:
                current_sum += nums[right]
                taken.add(nums[right])
                right += 1

                if right - left == k:
                    max_sum = max(max_sum , current_sum)
                    current_sum -= nums[left]
                    taken.remove(nums[left])
                    left += 1
            
            else:
                current_sum -= nums[left]
                taken.remove(nums[left])
                left += 1

        return max_sum
        # count = collections.Counter()
        # ans,l = 0,0
        # res = 0
        # n = len(nums)
        # for i in range(n):
        #     ans += nums[i]
        #     if count[nums[i]] == 0:
        #         l += 1
        #     count[nums[i]] += 1
        #     if i >= k:
        #         ans -= nums[i-k]
        #         count[nums[i-k]] -= 1
        #         if count[nums[i-k]] == 0:
        #             l -= 1
        #     if i >= k-1:
        #         if l == k:
        #             res = max(res, ans)
        # return res