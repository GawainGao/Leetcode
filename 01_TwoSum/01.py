class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for i in range(len(nums) - 1):
            if target - nums[i] in hash_map:
                return [hash_map[target - num[i]], i]
            hash_map[nums[i]] = i
