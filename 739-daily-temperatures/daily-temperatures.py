class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack =  []
        a = [0 for i in range(len(temperatures))]
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp,index = stack.pop()
                a[index] = i - index
            stack.append([t,i])
        return a

            


        # t = len(temperatures)
        # for i in t:
        #     if not stack or stack[-1] > temperatures(i):
        #         stack.push(temperatures[i])
        #     else :
        #         stack.pop()
        #         a[i] = 

            