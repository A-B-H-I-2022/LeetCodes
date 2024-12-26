class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = s.split()
        for i in ans[::-1]:
            return len(i)