#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        if len(haystack) == 0: return -1
        if needle == haystack: return 0
        for i in range(len(haystack)-len(needle)+1):
            for pos in range(len(needle)):
                if needle[pos] != haystack[pos+i]:
                    break
                if pos == len(needle) - 1:
                    return i
        return -1


        
        
