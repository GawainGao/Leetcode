class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag = True
        for i in range(9):
            flag = flag and self.isRepeat(self.getNumsInRow(board, i)) and self.isRepeat(self.getNumsInLine(board, i))
        for i in range(0,8,3):
            for j in range(0,8,3):
                flag = flag and self.isRepeat(self.getNumsInSquare(board,i,j))
        return flag
        
        
    def isInOneLine(self, board: List[List[str]], dire):
        #dire: direction, true=verticle
        #n_line: nth line
        pass
        
    def getNumsInSquare(self, board, i, j):
        res = []
        for ii in range(i, i+3):
            for jj in range(j, j+3):
                if board[ii][jj] != '.':
                    res.append(board[ii][jj])
        return res
        
    def getNumsInRow(self, board, th):
        res = []
        for i in board[th]:
            if i != '.':
                res.append(i)
        return res
    
    def getNumsInLine(self, board, th):
        res = []
        for i in board:
            if i[th] != '.':
                res.append(i[th])
        return res
        
    def isRepeat(self, nums):
        li = []
        for i in nums:
            if i in li:
                return False
            else:
                li.append(i)
        return True