#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        num_change_rule = {}
        for i in range(97, 123):
            num_change_rule[chr(i)] = pow(5, i - 97)               
        
        result = {}
        for s in strs:
            sp = 0
            for j in range(len(s)):
                sp += num_change_rule[s[j]]
            if sp in result:
                result[sp].append(s)
            else:
                result[sp] = []
                result[sp].append(s)

        resultDict = []
        for key in result:
            resultDict.append(result[key])
        return resultDict

# ✔ Accepted
#   ✔ 101/101 cases passed (112 ms)
#   ✔ Your runtime beats 80.89 % of python3 submissions
#   ✔ Your memory usage beats 43.4 % of python3 submissions (16.7 MB)

