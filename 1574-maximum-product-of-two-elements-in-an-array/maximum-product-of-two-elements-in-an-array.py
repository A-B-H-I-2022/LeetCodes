class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b = 0,0
        heapq.heapify(nums)
        while len(nums) > 2:
            heapq.heappop(nums)
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        return (a-1)*(b-1)
        