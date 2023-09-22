class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        lisx = []
        lisy = []
        ans = []
        for i in range(20):
            if x**i <= bound:
                lisx.append(x**i)
            else:
                break
        for i in range(20):
            if y**i <= bound:
                lisy.append(y**i)
            else:
                break
        for i in lisx:
            for j in lisy:
                if (i + j <= bound):
                    ans.append(i + j)
        return list(set(ans))

    
        