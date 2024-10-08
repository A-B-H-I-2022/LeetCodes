class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in nums:
            heapq.heappush(heap,i)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
        # nums.sort()
        # return nums[-k]