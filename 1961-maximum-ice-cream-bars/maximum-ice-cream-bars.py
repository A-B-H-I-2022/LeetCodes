class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        l = len(costs)
        for i in range(l):
            coins -= costs[i]
            if coins < 0:
                return i
        return l
        # answer,count = 0,0
        # ans = []
        # if sum(costs) <= coins:
        #     return len(costs)
        # else:
        #     costs.sort()
        #     for i in costs:
        #         answer += i
        #         if answer <= coins:
        #             count += 1
        #         else:break
        # return count
