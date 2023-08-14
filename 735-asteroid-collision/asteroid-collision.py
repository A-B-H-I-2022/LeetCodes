class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        j = 0
        n = len(asteroids)

        for i in range(n):
            asteroid = asteroids[i]
            while j > 0 and asteroids[j - 1] > 0 and asteroid < 0 and asteroids[j - 1] < abs(asteroid):
                j -= 1

            if j == 0 or asteroid > 0 or asteroids[j - 1] < 0:
                asteroids[j] = asteroid
                j += 1
            elif asteroids[j - 1] == abs(asteroid):
                j -= 1
        return asteroids[:j]



        # l = len(asteroids)
        # i = 0
        # if l == 0 or l == 1:
        #     return asteroids
        # else:
        #     while i < len(asteroids):
        #         if asteroids[i]<0:
        #             if abs(asteroids[i-1]) > abs(asteroids[i]):
        #                 asteroids.pop(i)
        #                 i -= 1
        #                 # l -= 1
        #             elif abs(asteroids[i-1]) < abs(asteroids[i]):
        #                 asteroids.pop(i-1)
        #                 i -= 2
        #                 # l -= 1
        #                 if i < 0:break
        #             else:
        #                 asteroids.pop(i)
        #                 asteroids.pop(i-1)
        #                 i -= 3
        #                 # l -= 2
        #         # if i < l-1:
        #         i += 1
        #         # else:break
        # return asteroids
