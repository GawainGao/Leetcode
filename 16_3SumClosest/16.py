class Solution(object):
    def threeSumClosest(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
        nums.sort()
        s,left,right = 0,0,0
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            while left != right:
                s = nums[left] + nums[right] + nums[i]
                if s == target:
                    return s
                elif s > target:
                    if s-target < abs(res-target):
                        res = s
                    right -= 1
                else:
                    if target-s < abs(res-target):
                        res = s
                    left += 1
        return res

