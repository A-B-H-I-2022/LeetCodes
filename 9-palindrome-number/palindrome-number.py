class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        flag = 0
        for i in range(len(y)):
            if y[i] != y[-i-1] :
                return False
            else:
                flag = 0
        if flag == 0:
            return True
        