class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        while True:
            current = nums[pos]
            if current == 0:
                break
            nums[pos] = 0
            pos = current
        return pos
