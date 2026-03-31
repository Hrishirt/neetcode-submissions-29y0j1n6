class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [0] * len(nums)
        after = [0] * len(nums)
        prod = [0] * len(nums)

        before[0] = after[-1] = 1 

        for x in range(1,len(nums)):
            before[x] = nums[x-1] * before[x-1]
        for x in reversed(range(len(nums) -1)):
            after[x] = nums[x + 1] * after[x +1]
        
        for x in range(len(nums)):
            prod[x] = after[x] * before[x]
        return prod