class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x>0 and x%10 == 0):
            return False
        ans = 0
        while x > ans:
            ans = 10*ans + x%10
            x = x//10
        return x == ans or x == ans//10
        # y = str(x)
        # flag = 0
        # for i in range(len(y)):
        #     if y[i] != y[-i-1] :
        #         return False
        #     else:
        #         flag = 1
        # if flag:
        #     return True
        