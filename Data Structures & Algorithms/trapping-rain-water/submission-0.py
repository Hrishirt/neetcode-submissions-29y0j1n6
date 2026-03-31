class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        final = [0] * n
        mins = [0] * n

        for x in range(1,n):
            maxLeft[x] = max(height[0:x])
        current_max = 0 
        for x in range(n - 1, -1, -1):
            maxRight[x] = current_max
            current_max = max(current_max, height[x])
        
        for x in range(n):
            mins[x] = min(maxLeft[x], maxRight[x])
        
        for x in range(n):
            final[x] = 0 if mins[x] <= height[x] else mins[x] - height[x]
        
        area = 0 
        for num in final:
            area += num 
        return area