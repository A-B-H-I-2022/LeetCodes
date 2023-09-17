class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in map:
                # print(map) key:num value ; value:index
                return [i,map[a]]
            map[nums[i]] = i

                    