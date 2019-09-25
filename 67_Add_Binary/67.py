class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la = len(a)
        lb = len(b)
        f = 'a' if la > lb else 'b'
        c = max(la,lb) - min(la,lb)
        el = '0' * c
        if f == 'a':
            b = el + b
            l = la
        else:
            a = el + a
            l = lb
        flag = 0
        res = []
        for i in range(l-1, -1, -1):
            if int(a[i]) + int(b[i]) + flag >= 2:
                res.append((int(a[i])+int(b[i])+flag)%2)
                flag = 1
            else:
                res.append(int(a[i])+int(b[i])+flag)
                flag = 0
        res.append(flag)
        res = res[::-1]
        resLIst = ''
        for i in res:
            resLIst = resLIst + str(i)
        if resLIst[0] == '0':
            resLIst = resLIst[1:]
        return resLIst
        