class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        li = grid
        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    li[j][i] = grid[j][i]
                elif i == 0:
                    li[j][i] = li[j-1][i] + grid[j][i] 
                elif j == 0:
                    li[j][i] = li[j][i-1] + grid[j][i]
                else:
                    li[j][i] = min(li[j-1][i],li[j][i-1]) + grid[j][i]
        print(li)
        return li[j][i]
    