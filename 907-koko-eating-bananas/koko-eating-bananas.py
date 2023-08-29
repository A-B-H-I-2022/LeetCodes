class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        # """
        # print(math.ceil(4/3))
        # l,r = 1,max(piles) 
        # a = 0
        # while l < r:
        #     k = (l+r)//2
        #     hours = 0
        #     for i in piles:
        #         hours += math.ceil(i / k)+1
        #     if hours <= h:
        #         a = k
        #         r = k
        #     else:
        #         l = k + 1
        # return l

        l=1
        r=max(piles)
        while l<r:
            mid=(l+r)//2
            c=0
            for j in piles:
                c+=((j-1)//mid)+1
            if c>h:
                l=mid+1
            else:
                r=mid
        return l