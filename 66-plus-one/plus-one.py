class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        given = 0
        l = len(digits)-1
        for i in digits:
            given += i*(10**l)
            l -= 1 
        given += 1

        ans = []
        
        while given > 0:
            a = given % 10
            given = given // 10
            ans.append(a)
        
        return ans[::-1]