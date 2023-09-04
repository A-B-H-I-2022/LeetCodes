class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = len(s)-1
         
        while i < j and s[i] == s[j]:
            k = s[i]
            while i < len(s) and s[i] == k:
                i += 1
            while j >= 0 and s[j] == k:
                j -= 1
        if j<i:
            return 0
        return j-i+1
            