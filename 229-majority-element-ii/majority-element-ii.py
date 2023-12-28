class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        map = Counter(nums)
        ans = []
        t = len(nums) // 3
        for k,v in map.items():
            if v > t:
                ans.append(k)
        return ans
        