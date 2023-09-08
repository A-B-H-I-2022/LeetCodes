class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a = 0
        l = 0 
        r = len(height)-1
        h = max(height)
        while l < r:
            area= (r-l)*(min(height[l],height[r]))
            a = max(a,area)  
            if (height[l]<height[r]):
                l += 1
            else :
                r -= 1
            if (r-l) * h <= a:
                break 
        return a
        
        
        #a = 0
        #n = []
        #h = len(height)
        #for i in range(h-1):
        #  for j in range(i+1,h):
        #        s1 = min(height[i],height[j])
        #        s2 = j-i
        #       n.append(s1*s2)
        #return max(n)
