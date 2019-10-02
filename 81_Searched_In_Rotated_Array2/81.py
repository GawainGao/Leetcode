class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return False
        if nums[0] == target: return True
        if len(nums) == 1:
            return True if nums[0] == target else False
        start = 0
        end = len(nums)-1
        mid = (start + end) // 2    
        
        while start != end:
            if nums[start] == nums[end]:
                end -= 1 
                continue
            if nums[start] == target: return True
            if nums[end] == target: return True
            if nums[mid] == target: return True
            mid = (start + end) // 2
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
        return False