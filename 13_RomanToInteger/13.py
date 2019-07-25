class Solution(object):
    def romanToInt(self, s):
        """
            :type s: str
            :rtype: int
            """
        numerals = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        suum = 0
        prev = 10000
        for x in s:
            if numerals[x] > prev:
                suum = suum - 2 * prev + numerals[x]
            else:
                suum = suum + numerals[x]
            prev = numerals[x]
        return suum
