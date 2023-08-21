class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        a = Counter(word1)
        b = Counter(word2)
        c1 = sorted(a.values())
        c2 = sorted(b.values())
        if c1 == c2 and set(word1) == set(word2):
            return True
        return False