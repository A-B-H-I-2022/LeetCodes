class Solution(object):
    def containsDuplicate(self, nums):
        answer = len(list(set(nums)))
        ans = len(nums)
        if answer < ans:
            return True
        else:
            return False



























        # a = list(set(nums))
        # l = len(a)
        # m = len(nums)
        # if l < m:
        #     return True
        # else:
        #     return False