class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
            :type s: str
            :rtype: int
            """
        start = 0
        end = 0
        ans = 0
        countDict = {}
        for i in s:
            end = end + 1
            countDict[i] = countDict.get(i,0) + 1
            while countDict[i] > 1:
                countDict[s[start]] -= 1
                start = start + 1
            ans = max(ans,end - start)
        return ans
