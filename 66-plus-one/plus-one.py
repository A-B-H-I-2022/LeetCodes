class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits


        # given = 0
        # l = len(digits)-1
        # for i in digits:
        #     given += i*(10**l)
        #     l -= 1 
        # given += 1

        # ans = []
        
        # while given > 0:
        #     a = given % 10
        #     given = given // 10
        #     ans.append(a)
        
        # return ans[::-1]