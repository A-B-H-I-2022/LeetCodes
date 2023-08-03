class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            map[key].append(s)
        return list(map.values())