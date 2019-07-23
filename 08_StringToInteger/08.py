class Solution(object):
    def myAtoi(self, str):
        """
            :type str: str
            :rtype: int
            """
        if not str:
            return 0
        str = str.strip()
        s = 0
        flag = 1
        if len(str) == 1:
            if str[0] >='0' and str[0]<='9': return ord(str[0])-ord('0')
            else: return 0
        if str[0] == '-':
            str = str[1:]
            flag = -1
        elif str[0] == '+':
            str = str[1:]
        for c in str:
            if c >='0' and c<='9':
                s = 10 * s + ord(c) - ord('0')
            else:
                break
        s = s * flag
        s = s if s <=2147483647 else 2147483647
        s = s if s >=-2147483648 else -2147483648
        return s
