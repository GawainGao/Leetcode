class Solution(object):
    def longestPalindrome(self, s):
        """
            :type s: str
            :rtype: str
            """
        if s[0] == None:
            return None
        cache = s[0]
        m = 1
        l = len(s)
        start,end = 0,0
        for i in range(l):
            for k in range(min((l-i-1),i)+1):
                if k == 0:
                    pass
                elif s[i-k] == s[i+k]:
                    start = i - k
                    end = i + k
                    if m < (2*k + 1):
                        m = 2*k + 1
                        cache = s[start:end+1]
                else:
                    break
        for i in range(l-1):
            if s[i] == s[i + 1]:
                if m == 1:
                    m = 2
                    cache = s[i:i+2]
                for k in range(min(i,(l-i-2))+1):
                    if k == 0:
                        pass
                    elif s[i-k] == s[i+1+k]:
                        start = i - k
                        end = i + k + 1
                        if m < (2*k+2):
                            m = 2*k+2
                            cache = s[start:end+1]
                    else:
                        break

    return cache
