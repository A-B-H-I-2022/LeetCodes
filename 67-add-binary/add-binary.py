class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        carry = 0
        ans = ""
         
        for i in range(max(len(a),len(b))):
            if i < len(a):
                A = ord(a[i]) - ord('0') 
            else:
                A = 0
            if i < len(b):
                B = ord(b[i]) - ord('0')
            else:
                B = 0
            total = A + B + carry
            char = str(total%2)
            ans = char + ans
            carry = total//2
        if carry:
            return "1" + ans
        return ans