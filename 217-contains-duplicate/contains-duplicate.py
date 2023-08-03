class Solution(object):
    def containsDuplicate(self, nums):
        a = list(set(nums))
        l = len(a)
        m = len(nums)
        if l < m:
            return True
        else:
            return False