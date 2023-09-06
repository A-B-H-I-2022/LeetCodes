class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return n
        prev2,prev=0,1
        for i in range(2,n+1):
            curr=prev+prev2
            prev2=prev
            prev=curr
        return curr