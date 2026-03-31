class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        for x in range(len(nums)): 
            if x > 0 and nums[x - 1] == nums[x]:
                continue
            l = x + 1
            r = len(nums) - 1 
            while l < r: 
                if nums[x] + nums[l] + nums[r] == 0:
                    output.append([nums[x], nums[l], nums[r]])
                    l += 1 
                    r -= 1 
                    while nums[l] == nums[l -1] and l < r:
                        l += 1  
                if nums[l] + nums[r] > 0 - nums[x]:
                    r -= 1 
                
                if nums[l] + nums[r] < 0 - nums[x]:
                    l += 1 
        return output