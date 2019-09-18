class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        li = [[0 for _ in range(m)] for _ in range(n)]
        for j in range(m):
            for i in range(n):
                if i == 0 or j==0:
                    li[i][j] = 1
                else:
                    li[i][j] = li[i-1][j] + li[i][j-1]
        return li[i][j]