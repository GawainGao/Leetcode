class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res_li = []
        self.r_combine([i + 1 for i in range(n)], k, [], res_li)
        return res_li
    def r_combine(self, li, k, res, res_li):
        if k == 0:
            res_li.append(res)
        else:
            for i in range(len(li)):
                self.r_combine(li[i+1:], k-1, res+[li[i]], res_li)