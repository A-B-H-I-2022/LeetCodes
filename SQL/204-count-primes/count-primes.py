class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        seen, ans = [0] * n, 0
        for num in range(2, n):
            if seen[num]: continue
            ans += 1
            seen[num*num:n:num] = [1] * ((n - 1) // num - num + 1)
        return ans


        # count = 1
        # flag = 0
        # if n < 3:
        #     return 0
        # elif n >= 3:
        #     for i in range(3,n):
        #         for j in range(2,i):
        #             if i%j == 0:
        #                 flag = 1
        #         if not flag:
        #             count += 1
        #         flag = 0
        # return count

                        
        