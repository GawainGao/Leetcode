class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res_list = []
        self.r_subsets(nums, [], res_list)
        return res_list
    
    
    def r_subsets(self, nums, res, res_list):
        
        if len(nums) == 0:
            res_list.append(res)
        else:
            res_list.append(res)
            for i in range(len(nums)):
                self.r_subsets(nums[i+1:], res+[nums[i]], res_list)