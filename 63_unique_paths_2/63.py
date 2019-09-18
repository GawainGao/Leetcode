class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        li = obstacleGrid
        for i in range(n):
            for j in range(m):
                if obstacleGrid[j][i] == 1:
                    li[j][i] = 0
                else:
                    if i == j == 0:
                        li[j][i] = 1
                    elif i == 0:
                        li[j][i] = li[j-1][i]
                    elif j == 0:
                        li[j][i] = li[j][i-1]
                    else:
                        li[j][i] = li[j-1][i] + li[j][i-1]    
        return li[j][i]
        
        
        
        