class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1 

        while l <= r: 
            k = (l + r) // 2 

            if nums[k] == target:
                return k 

            if nums[l] <= nums[k]:
                if nums[k] < target or target < nums[l]:
                    l = k + 1 
            
                else:
                    r = k - 1 
            
            else:
                if nums[k] < nums[r]:
                    if nums[k] > target or target > nums[r]:
                        r = k - 1 
                    else:
                        l = k + 1 
        return -1 