class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        heap = [(-v, k) for k, v in count.items()]
        heapq.heapify(heap)
        ans = []
        while heap:
            v, k = heapq.heappop(heap)
            ans += [k] * -v
        return ''.join(ans)