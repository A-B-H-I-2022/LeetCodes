class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        map = {}
        for i in range(len(s)):
            map[s[i:i+10]] = 1 + map.get(s[i:i+10], 0)
        return [key for key, value in map.items() if value > 1]