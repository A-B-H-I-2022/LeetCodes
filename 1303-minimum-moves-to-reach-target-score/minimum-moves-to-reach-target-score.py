class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        # t1 = target
        # stack = []
        # i = 1
        # ans = 0
        # if maxDoubles == 0:
        #     return target-1
        # for i in range(maxDoubles):
        #     t1 -= t1//2 + 1 if t1%2 != 0 else t1//2
        #     stack.append(t1)
        # while i < target:
        #     if stack:
        #         t2 = stack.pop()
        #         ans += t2-i
        #         i = t2
        #         i = i*2
        #         maxDoubles -= 1
        #     ans += 1
        # return ans

        res = 0
        while maxDoubles > 0 and target > 1:
            if target&1==1:
                target = target - 1
            else:
                target = target / 2
                maxDoubles = maxDoubles - 1
            res = res + 1
        return  res + (target-1)