class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        length = len(s)
        def pal(l,r):
            while l >=0 and r < length and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        for i in range(length):     
            pal1 = pal(i, i)
            pal2 = pal(i, i+1)
           
            if len(pal1) > len(result):
               result = pal1
            if len(pal2) > len(result):
                result = pal2
        return result