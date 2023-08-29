class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        map = {}
        ans,r = 0,0
        for i in answers:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        for k,v in map.items():
            if k == 0:
                ans += v
            else:
                if v > k+1:
                    ans += (v//(k+1))*(k+1)
                    if v%(k+1) != 0:
                        ans += k+1
                        print(ans)
                else:
                    ans += k+1
        return ans

            

        # map = {}
        # ans = 0
        # for i in answers:
        #     if i in map and i != 0:
        #         map[i] += 1
        #     elif i in map and i == 0:
        #         ans += 1
        #     else:
        #         map[i] = 1
        #         ans += i + 1
        # if 1 in map:
        #     if map[1] % 2 != 0 and map[1] > 1:
        #         return ans+2
        #     else:
        #         return ans
        # else:
        #     return ans