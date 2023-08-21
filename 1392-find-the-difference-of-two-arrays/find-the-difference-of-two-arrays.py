class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        lis = [[],[]]
        for i in nums1:
            if i not in nums2 and i not in lis[0]:
                lis[0].append(i)
        for j in nums2:
            if j not in nums1 and j not in lis[1]:
                lis[1].append(j)
        return lis