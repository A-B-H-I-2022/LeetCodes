class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            column = []
            for j in grid:
                column.append(j[i])
            ans += grid.count(column)
        return ans