class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        nums = sorted(nums)
        for index, num in enumerate(nums): 
            if index > 0 and nums[index - 1] == num:
                continue
            l,r = index + 1, len(nums) - 1 
            while l < r: 
                if nums[l] + nums[r] + num == 0: 
                    res.append([nums[l], nums[r], num])
                    l += 1 
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1 
                if nums[l] + nums[r] > 0 - num: 
                    r -= 1 
                if nums[l] + nums[r] < 0 - num: 
                    l += 1 
        return res