class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        
        answer,count = 0,0
        ans = []
        if sum(costs) <= coins:
            return len(costs)
        else:
            costs.sort()
            for i in costs:
                answer += i
                if answer <= coins:
                    count += 1
                else:break
        return count
