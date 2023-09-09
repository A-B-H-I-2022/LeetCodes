class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        dic = {0 : 1}
        summ = 0
        for i in nums:
            summ += i
            if summ - k in dic:
                count += dic[summ-k]
            if summ in dic:
                dic[summ] += 1
            else:
                dic[summ] = 1
        return count
        