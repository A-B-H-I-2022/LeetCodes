class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        nums = list(range(1,n+1))
        def solve(start):
            if start == n:
                self.count += 1
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                if nums[start]%(start+1) == 0 or (start+1)%nums[start] == 0:
                    solve(start+1)
                nums[start], nums[i] = nums[i], nums[start]
        solve(0)
        return self.count