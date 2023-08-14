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