# √ Accepted
# √ 315/315 cases passed (60 ms)
# √ Your runtime beats 74.36 % of python3 submissions
# √ Your memory usage beats 5.4 % of python3 submissions (14.3 MB)
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height.append(0)
        height.insert(0,0)
        if len(height) <= 2:
            return 0
        maxx = height[0]
        i = 0
        for t in range(len(height)):
            if maxx < height[t]:
                maxx = height[t]
                i = t
        
        temp = [0]
        left = height[0]
        s = 0
        flag = 0
        for x in range(1,i+1):
            if left > height[x]:
                temp.append(height[x])
            else:
                s += left * (x - flag - 1) - sum(temp)
                left = height[x]
                flag = x
                temp = [0]
        right = height[-1]
        flag = len(height) - 1
        for x in range(len(height)-1, i-1, -1):
            if right > height[x]:
                temp.append(height[x])
            else:
                s += right * (flag - x - 1) - sum(temp)
                right = height[x]
                flag = x
                temp = [0]
        return s
    
                       
                       
        
        

