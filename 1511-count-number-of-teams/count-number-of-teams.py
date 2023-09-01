from itertools import combinations
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        hrat = [0]*len(rating)
        lrat = [0]*len(rating)
        ans = 0
        for i in range(len(rating)-1):
            for j in range(i+1,len(rating)):
                if rating[j] > rating[i]:
                    hrat[i] += 1
                elif rating[j] < rating[i]:
                    lrat[i] += 1
        for i in range(len(rating)-1):
            for j in range(i+1,len(rating)):
                if rating[j] > rating[i]:
                    ans += hrat[j]
                elif rating[j] < rating[i]:
                    ans += lrat[j]
        return ans
        # ans = 0
        # c = combinations(rating, 3)
        # for i in c:
        #     if (i[0] > i[1] and i[1] > i[2]) or (i[0] < i[1] and i[1] < i[2]):
        #         ans += 1
        # return ans
        