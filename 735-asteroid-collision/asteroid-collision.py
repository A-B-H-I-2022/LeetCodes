class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        i,l,top = 0,len(asteroids),0
        while i < l:
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                flag = 1
                while flag:
                    if stack and stack[-1] > 0:
                        top = stack[-1]
                    else:
                        stack.append(asteroids[i])
                        flag = 0
                        break
                    if top > abs(asteroids[i]):
                        flag = 0
                    elif top == abs(asteroids[i]):
                        stack.pop()
                        flag = 0
                    else:
                        stack.pop()
            i += 1
        return stack


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
