#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        length = len(matrix)
        print(length)
        side = int((length - 1) / 2) if length % 2 else int(length / 2)
        print(side)
        for i in range(side):  #row
            print('i', i)
            for j in range(i, length - i - 1):   #line
                print('j', j)
                temp = matrix[i][j]
                matrix[i][j] = matrix[length-j-1][i]
                matrix[length-j-1][i] = matrix[length-i-1][length-j-1]
                matrix[length-i-1][length-j-1] = matrix[j][length-i-1]
                matrix[j][length-i-1] = temp
        return matrix

# ✔ Accepted
#   ✔ 21/21 cases passed (44 ms)
#   ✔ Your runtime beats 51.04 % of python3 submissions
#   ✔ Your memory usage beats 6.25 % of python3 submissions (13.8 MB)

