class Solution(object):
    def fourSum(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[List[int]]
            """
        Dict = {}
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i + 1,len(nums)-2):
                p = j + 1
                q = len(nums) - 1
                while p != q:
                    s = nums[p] + nums[q] + nums[i] + nums[j]
                    if s == target:
                        if [nums[i],nums[j],nums[p],nums[q]] not in res:
                            res.append([nums[i],nums[j],nums[p],nums[q]])
                    if s > target:
                        q -= 1
                    else:
                        p += 1
    return res
