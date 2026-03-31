class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n 
        res = [0] * n 
        pref[0], suff[-1] = 1, 1 
        for x in range(1,n):
            pref[x] = nums[x -1] * pref[x-1]
        for x in reversed(range(n-1)):
            suff[x] = nums[x + 1] * suff[x + 1]
        for x in range(n): 
            res[x] = suff[x] * pref[x]
        return res