class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglyNumber = [1] 
        i2, i3, i5 = 0, 0, 0

        for i in range(0, n):
            nextMutipleOf2 = uglyNumber[i2] * 2
            nextMutipleOf3 = uglyNumber[i3] * 3
            nextMutipleOf5 = uglyNumber[i5] * 5
            nextUglyNumber = min(nextMutipleOf2, nextMutipleOf3, nextMutipleOf5)
            uglyNumber.append(nextUglyNumber)
            #move the pointer to the next ugly number 
            if nextUglyNumber == nextMutipleOf2: 
                i2 += 1
            if nextUglyNumber == nextMutipleOf3: 
                i3 += 1
            if nextUglyNumber == nextMutipleOf5: 
                i5 += 1
            
        return uglyNumber[n - 1]

        # lis = [1]
        # map = {}
        # while n-1:
        #     a = heapq.heappop(lis)
        #     if a*2 not in map:
        #        heapq.heappush(lis, a*2)
        #        map[a*2] = 1
        #     if a*3 not in map:
        #         heapq.heappush(lis, a*3)
        #         map[a*3] = 1
        #     if a*5 not in map:
        #         heapq.heappush(lis, a*5)
        #         map[a*5] = 1
        #     n -= 1
        # return heapq.heappop(lis)


        