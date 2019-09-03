class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        flag = 0
            
        if dividend < 0:
            dividend = -dividend
            flag = 1
        if divisor < 0:
            divisor = -divisor
            flag += 1
            flag = flag % 2
        while dividend >= divisor * 100000:
            dividend -= divisor * 100000
            res += 100000
        while dividend >= divisor:
            dividend -= divisor 
            res += 1
        if flag:
            res = -res
        if res < -2 ** 31:
            return -2**31
        if res > 2 ** 31 - 1:
            return 2**31 - 1
        return res
