class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = 1
        B = ""
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            if s[i].isalnum():
                B += s[i].lower()
        for i in range(len(B)//2):
            if (B[i] != B[-i-1]):
                return 0
            else :
                flag = 1
        if flag == 1:
            return 1