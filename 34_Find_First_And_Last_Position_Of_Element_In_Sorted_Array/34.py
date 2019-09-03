class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)        
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return self.searchTwoSide(nums,mid)
            elif nums[mid] > target:
                end = mid
            else:
                start = mid + 1
        return -1, -1
    
    def searchTwoSide(self, nums: List[int], seed: int):
        s = seed
        e = seed
        while s>=0 and nums[s] == nums[seed]:
            s -= 1
        while e<=len(nums)-1 and nums[e] == nums[seed]:
            e += 1
        return s+1,e-1
            