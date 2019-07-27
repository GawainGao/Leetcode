class Solution(object):
    def threeSum(self, nums):
        """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
        
        
        
        res = set()
        nums.sort()
        if len(nums) < 3:
            return []
        if nums[0] >= 0 and nums[2] == 0:
            return[[0,0,0]]
        
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                if (nums[i] + nums[j] + nums[k]) == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif (nums[i] + nums[j] + nums[k]) > 0:
                    k -= 1
                else:
                    j += 1
        return list(res)

