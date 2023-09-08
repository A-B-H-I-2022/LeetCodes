class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        b = a[::-1]
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
        # y = str(x)
        # flag = 0
        # for i in range(len(y)):
        #     if y[i] != y[-i-1] :
        #         return False
        #     else:
        #         flag = 1
        # if flag:
        #     return True
        