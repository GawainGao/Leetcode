#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
import itertools
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        words_du = words[:]

        if len(words) == 0:
            return []
        if len(s) < len(words[0]):
            return []

        for i in range(len(s)-len(words)*len(words[0])+1):
            words = words_du[:]
            self.startSubstring(s, words, i, res)
            s = s[1:]
        return res
        
    def startSubstring(self, s, words, startpoint, res):
        if len(words) == 1:
            if s[:len(words)] is words[0]:
                res.append(startpoint)
                return

        if s[:len(words[0])] in words:
            words.remove(s[:len(words[0])])
            if len(words) == 0:
                res.append(startpoint)
                print(res)
                return
            self.startSubstring(s[len(words[0]):], words, startpoint, res)
    
        

