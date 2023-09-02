class Solution(object):
    def mostPopularCreator(self, creators, ids, views):
        """
        :type creators: List[str]
        :type ids: List[str]
        :type views: List[int]
        :rtype: List[List[str]]
        """
        total = collections.Counter()
        map = {}
         
        for c,i,v in zip(creators, ids, views):
            total[c] += v
            if c not in map:
                map[c] = (v, i)
            if v > map[c][0]:
                map[c] = (v, i)
            elif v == map[c][0] and i < map[c][1]:
                map[c] = (v, i)
        highest = max(total.values())

        result = []
        for c in total.keys():
            if total[c] == highest:
                result.append([c , map[c][1]])
        return result