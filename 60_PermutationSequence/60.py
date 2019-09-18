class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        if n == 1: return "1"
        if n == 2: return str(9*k+3)
        def times(t):
            if t == 1: return 1
            else: return t * times(t-1)
        flag = 0
        num = [1,2,3,4,5,6,7,8,9]
        
        for i in range(n,0,-1):
            if i == 1:
                res += str(num[0])
                break
            flag1 = num[(k-1)/times(i-1)]
            res += str(flag1)
            num.remove(flag1)
            k = k - (k-1)/times(i-1) * times(i-1)
        return res