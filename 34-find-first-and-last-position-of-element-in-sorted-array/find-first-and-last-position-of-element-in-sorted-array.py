class Solution(object):
    def searchRange(self, nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # def search(x):
        #     lo, hi = 0, len(nums)           
        #     while lo < hi:
        #         mid = (lo + hi) // 2
        #         if nums[mid] < x:
        #             lo = mid+1
        #         else:
        #             hi = mid                    
        #     return lo
        
        # lo = search(target)
        # hi = search(target+1)-1
        
        # if lo <= hi:
        #     return [lo, hi]
                
        # return [-1, -1]

        def find(last = True):
            l = 0
            r = len(nums)-1
            ans = -1
            while l <=r:
                m = (l + r)//2
                if nums[m] < target:
                    l = m+1
                elif nums[m] > target:
                    r = m-1
                else:
                    ans = m
                    if last:
                        l = m +1
                    else:
                        r = m -1
            
            return ans
        
        
        return [find(False),find(True)]