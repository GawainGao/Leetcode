#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x
        if n < 0: n, x = -n, 1/x
        t = (n - 1) / 2 if n % 2 else n / 2
        res = self.myPow(x, t)
        return res * res * x if n % 2 else res * res 


# ✔ Accepted
#   ✔ 304/304 cases passed (36 ms)
#   ✔ Your runtime beats 72.85 % of python3 submissions
#   ✔ Your memory usage beats 6.9 % of python3 submissions (13.9 MB)
