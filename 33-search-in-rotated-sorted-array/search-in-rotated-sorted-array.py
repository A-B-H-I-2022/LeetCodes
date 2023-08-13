class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        l,r = 0,length - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else :
                r = mid - 1
        pivot = l
        def bs(left,right,target):
            l,r = left,right
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else :
                    l = mid + 1
            return -1

        n1 = bs(0,pivot-1,target)
        n2 = bs(pivot,length-1,target)
        if n1 != -1:
            return n1
        else:
            return n2