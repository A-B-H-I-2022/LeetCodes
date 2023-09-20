class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lis = [1]
        map = {}
        while n-1:
            a = heapq.heappop(lis)
            if a*2 not in map:
               heapq.heappush(lis, a*2)
               map[a*2] = 1
            if a*3 not in map:
                heapq.heappush(lis, a*3)
                map[a*3] = 1
            if a*5 not in map:
                heapq.heappush(lis, a*5)
                map[a*5] = 1
            n -= 1
        return heapq.heappop(lis)


        