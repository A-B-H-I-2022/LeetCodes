class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        j = 0
        l = len(pushed)
        for i in range(l):
            stack.append(pushed[i])
            while j < l:
                if stack:
                    k = stack[-1]
                if k == popped[j]:
                    stack.pop()
                    j += 1
                else:
                    break
        if j == l and not stack:
            return True
        else:
            return False 
        