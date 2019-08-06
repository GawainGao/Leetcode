#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = (start + end) // 2
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1 

        while start != end:
            if nums[start] == target: return start
            if nums[end] == target: return end
            if nums[mid] == target: return mid
            mid = (start + end) // 2
            print('start:',start,' mid:',mid,' end',end)
            if nums[start] < target < nums[mid]:
                end = mid - 1
                continue
            if target < nums[start] < nums[mid]:
                start = mid + 1
                continue
            if nums[start] < nums[mid] < target:
                start = mid + 1
                continue
            if nums[start] > target > nums[mid]:
                start = mid + 1
                continue
            if target > nums[start] > nums[mid]:
                end = mid - 1
                continue
            if nums[start] > nums[mid] > target:
                end = mid - 1
                continue
            start += 1
        return -1

