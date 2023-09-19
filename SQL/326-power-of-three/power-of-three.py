class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n>0) and 1162261467%n == 0
        # x = 1
        # if n <= 0 :
        #     return False
        # elif n == 1:
        #     return True
        # else:
        #     while x < n:
        #         x = x*3
        #         if x == n:
        #             return True
        #     return False
                

        