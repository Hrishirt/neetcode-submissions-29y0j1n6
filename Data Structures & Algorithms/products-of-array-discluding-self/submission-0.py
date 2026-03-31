class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n 
        pref = [0] * n 
        suff = [0] * n 

        pref[0] = suff[n-1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in reversed(range(len(nums) - 1)):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        for i in range(len(nums)):
            res[i] = pref[i] * suff[i]
        
        return res