class Solution:
    def mySqrt(self, x: int) -> int:
        count = 0
        while True:
            if count * count > x:
                return count - 1
            count += 1