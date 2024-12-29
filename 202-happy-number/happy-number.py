class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        hset = set()
        while n != 1:
            if n in hset: return False
            hset.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True
        # nodes = set()
        # a = n
        # sum = 0
        # while n not in nodes:
        #     nodes.add(n)
        #     while a:
        #         r = a%10
        #         r = r**2
        #         sum += r
        #         a /= 10
        #     a = sum
        #     sum = 0
        #     if n == 1:
        #         return True
        # return False



        