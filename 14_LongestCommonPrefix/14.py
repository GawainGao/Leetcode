class Solution(object):
    def longestCommonPrefix(self, strs):
        """
            :type strs: List[str]
            :rtype: str
            """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        miniSize = len(strs[0])
        for eachStrs in strs:
            if len(eachStrs) < miniSize:
                miniSize = len(eachStrs)
        print miniSize
        if miniSize == 0:
            return ''
        res = ''
        for j in range(miniSize):
            flag = strs[1][j]
            for i in range(len(strs)):
                if flag == strs[i][j]:
                    pass
                else:
                    return res
                print j
            res = res + flag
        return res
