class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        print(m, n)
        for j in range(m):
            for i in range(n):
                if (0 not in matrix[j]) and (0 not in [x[i] for x in matrix]):
                    matrix[j][i] = str(matrix[j][i])
        print(matrix)
        for i in range(m):
            for j in range(n):
                if isinstance(matrix[i][j],str):
                    matrix[i][j] = int(matrix[i][j])
                else:
                    matrix[i][j] = 0    
                    