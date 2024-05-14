class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if '0' in [num1, num2]:
            return '0'
        
        def chartoint(n):
            ans = 0
            for i in n:
                ans = ans*10 + (ord(i) - ord('0'))
            return ans

        def inttochar(s):
            res = ''
            while s:
                a = s%10
                s = s//10
                res = chr(ord('0') + a) + res
            return res
            
        return inttochar(chartoint(num1)*chartoint(num2))