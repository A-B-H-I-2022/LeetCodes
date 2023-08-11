class Solution(object):
    def searchRange(self, nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid                    
            return lo
        
        lo = search(target)
        hi = search(target+1)-1
        
        if lo <= hi:
            return [lo, hi]
                
        return [-1, -1]





        # left,right = 0,len(nums)-1
        # a = []
        # lb,ub = 0,0
        # if len(nums) == 0:
        #     return [-1,-1]
        # else:
        #     while left <= right:
        #         mid = (left + right)//2
        #         if nums[mid] == target:
        #             lb,ub = mid,mid
        #             break
        #         elif nums[mid] > target:
        #             right = mid - 1
        #         else :
        #             left = mid + 1  






        #     def binarySearch(arr, l, r, x):
 
        #         # Check base case
        #         if r >= l:
 
        #             mid = l + (r - l) // 2
 
        #             # If element is present at the middle itself
        #             if arr[mid] == x:
        #                 return mid
 
        #             # If element is smaller than mid, then it
        #             # can only be present in left subarray
        #             elif arr[mid] > x:
        #                 return binarySearch(arr, l, mid-1, x)
 
        #             # Else the element can only be present
        #             # in right subarray
        #             else:
        #                 return binarySearch(arr, mid + 1, r, x)
 
        #         # Element is not present in the array
        #         else:
        #             return -1
        # index = int(binarySearch(nums, 0, len(nums)-1, target))
        # #print(index) 

        # lb,ub = index,index
        # while(nums[lb] != target):
        #     if nums[lb-1] == target:
        #         lb = lb-1

        # while(nums[ub] != target):
        #     if nums[ub+1] == target:
        #         ub = ub+1
             
        # return [lb,ub]