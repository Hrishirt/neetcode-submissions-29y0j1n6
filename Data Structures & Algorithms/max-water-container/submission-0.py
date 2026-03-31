class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0 
        for c1 in range(len(heights)):
            for c2 in range(c1+ 1,len(heights)):
                area = min(heights[c1], heights[c2]) * (c2 - c1) 
                maxArea = max(maxArea, area)
        return maxArea 