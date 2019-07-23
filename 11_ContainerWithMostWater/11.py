class Solution(object):
    def maxArea(self, height):
        """
            :type height: List[int]
            :rtype: int
            """
        start = 0
        end = len(height) - 1
        area = 0
        while start != end:
            area = max(area,(end-start)*min(height[end],height[start]))
            if height[start] < height[end]: start += 1
            else: end -= 1
        return area



