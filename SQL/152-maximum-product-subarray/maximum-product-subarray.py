class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum, maximum = 1,1
        result = max(nums)
        for i in nums:
            temp = maximum*i
            maximum = max(maximum*i , minimum*i , i)
            minimum = min(temp , minimum*i , i)
            result = max(result , maximum)
        return result



        # a = []
        # l,i,m = len(nums),0,0
        # if l == 1:
        #     return nums[0]
        # else:
        #     while i <= l-1:
        #         x = nums[i]
        #         a.append(x)
        #         for j in range(i+1,l):
        #             x = x*nums[j]
        #             a.append(x)
        #         i += 1
        # return max(a)
