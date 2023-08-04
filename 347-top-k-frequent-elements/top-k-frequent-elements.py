class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        values = {}
        freq = [[] for i in range(len(nums)+1)]
        for v in nums:
            if v in values:
                values[v]+=1
            else:
                values[v]=1
        for key,v in values.items():
            freq[v].append(key)
        a = []
        for i in range(len(freq)-1,0,-1):
            for key in freq[i]:
                a.append(key)
                if len(a)==k:
                    return a