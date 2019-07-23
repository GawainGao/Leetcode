class Solution(object):
    def reverse(self, x):
        """
            :type x: int
            :rtype: int
            """
        minus = 0
        if x < 0:
            x = -x
            minus = 1
        res = 0
        flag = 0
        while x:
            flag = x % 10
            x = x / 10
            res = res * 10 + flag
        if minus:
            res = -res
        if res <= 0x7fffffff and res >= -0x7fffffff-1:
            return res
        else:
            return 0
