class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s1 = ''
        # for c in s.lower():
        #     if c.isalnum():
        #         s1 += c

        # return True if s1==s1[::-1] else False

        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        reversed_s = s[::-1]

        if s == reversed_s:
            return True

        return False

        # flag = 1
        # B = ""
        # if len(s) == 0:
        #     return 0
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         B += s[i].lower()
        # for i in range(len(B)//2):
        #     if (B[i] != B[-i-1]):
        #         return 0
        #     else :
        #         flag = 1
        # if flag == 1:
        #     return 1
