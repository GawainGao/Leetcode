#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                flag = i
                break
        if flag:
            for i in range(len(nums)-1, flag-1, -1):            
                if nums[i] > nums[flag-1]:
                    temp = nums[i]
                    nums[i] = nums[flag-1]
                    nums[flag-1] = temp
                    print(nums)
                    break
            du = nums[flag:]
            du.sort()
            nums[flag:] = du  
        else:
            nums.reverse()
