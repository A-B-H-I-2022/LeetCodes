class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        ans = [0]*(n + 1)
        for i, j, k in bookings:
            ans[i-1] += k
            ans[j] -= k
        for i in xrange(1, n):
            ans[i] += ans[i - 1]
        return ans[:-1]





        # x,y,z = 0,0,0
        # lis = [0]*(n+1)
        # for i in bookings:
        #     x,y,z = i[0],i[1],i[2]
        #     while  x <= y:
        #         lis[x-1] += z
        #         x += 1
        # return lis[:-1]  