class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        value = [v for v in Counter(arr).values()]
        return len(value) == len(set(value))
        # map = {}
        # l = []
        # for i in arr:
        #     if i in map:
        #         map[i] += 1
        #     else:
        #         map[i] = 1
        # for v in map.values():
        #     l.append(v)
        
        # if len(l) != len(set(l)):
        #     return False
        # else:
        #     return True
           