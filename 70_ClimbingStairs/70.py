class Solution:
    def climbStairs(self, n: int) -> int:
        res = []
        res.append(1)
        res.append(2)
        for i in range(2,n):
            res.append(res[i-1]+res[i-2])
        return res[n-1]
        
   