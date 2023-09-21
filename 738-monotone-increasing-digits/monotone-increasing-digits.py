class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = []
        if n < 10:
            return n
        for i,c in enumerate(str(n)):
            l.append(int(c))
        n = len(l)
        for i in range(n-1,0,-1):
            if l[i] < l[i-1]:
                l[i-1] -= 1
                for i in range(i,n):
                    l[i] = 9
        ans = ''.join([str(x) for x in l])
        return int(ans)