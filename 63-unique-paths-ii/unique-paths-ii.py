class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        ans = [[0]*c for _ in range(r)]
        for i in range(r):
            if obstacleGrid[i][0] == 0:
                ans[i][0] = 1
            else:
                break
        for j in range(c):
            if obstacleGrid[0][j] == 0:
                ans[0][j] = 1
            else:
                break
        for i in range(1,r):
            for j in range(1,c):
                if obstacleGrid[i][j] == 0:
                    ans[i][j] = ans[i-1][j] + ans[i][j-1]
        return ans[r-1][c-1]