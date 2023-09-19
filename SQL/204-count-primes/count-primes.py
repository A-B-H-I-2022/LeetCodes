class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                is_prime[i*i:n:i] = [False] * len(is_prime[i*i:n:i])

        return sum(is_prime)

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

                        
        