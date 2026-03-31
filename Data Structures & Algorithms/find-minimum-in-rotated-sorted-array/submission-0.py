class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0] 
        for num in nums:
            if num < minVal:
                minVal = num 
        return minVal 
