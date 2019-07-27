class Solution(object):
    def isValid(self, s):
        """
            :type s: str
            :rtype: bool
            """
        res = []
        for i in s:
            if i == "[" or i == "{" or i == "(":
                res.append(i)
            elif i == "]" :
                if res == [] or res.pop() != "[": return False
            elif i =="}":
                if res == [] or res.pop() != "{": return False
            elif i ==")":
                if res == [] or res.pop() != "(": return False
        if  res == []: return True
        else: return False
