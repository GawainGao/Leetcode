class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = 0
        for i in range(len(nums)):
            if i > right: return False
            right = max(right, i + nums[i])
        return True    