class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        # """

        l,r = 1,max(piles) 
        while l < r:
            k = (l+r)//2
            hours = 0
            for i in piles:
                hours += ((i-1) // k) + 1
            if hours > h:
                l = k + 1 
            else:
                r = k
        return l

        # l,r = 1,max(piles) 
        # while l < r:
        #     k = (l+r)//2
        #     hours = 0
        #     for i in piles:
        #         hours += ((i-1)//k)+1
        #     if hours > h:
        #           l = k + 1
        #     else:
        #         r = k
        # return l