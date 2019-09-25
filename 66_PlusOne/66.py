class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ''
        for i in digits:
            res = res + str(i)
        res = int(res)
        res += 1
        resLIst = []
        res = str(res)
        for i in res:
            resLIst.append(int(i))
        return resLIst