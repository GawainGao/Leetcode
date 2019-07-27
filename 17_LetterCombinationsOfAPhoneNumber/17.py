class Solution(object):
    def letterCombinations(self, digits):
        """
            :type digits: str
            :rtype: List[str]
            """
        
        if not digits:
            return []
        result = []
        self.dfs(digits, "", result)
        return result
    
    def dfs(self,digits,current,result):
        if not digits:
            result.append(current)
            return
        for c in self.ddict[digits[0]]:
            self.dfs(digits[1:],current+c,result)


ddict = {'2':['a','b','c'],
'3':['d','e','f'],
'4':['g','h','i'],
'5':['j','k','l'],
'6':['m','n','o'],
'7':['p','q','r','s'],
'8':['t','u','v'],
'9':['w','x','y','z']
}

