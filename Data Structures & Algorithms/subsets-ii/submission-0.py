class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        sub = [] 
        nums.sort()
        def backtrack(i):
            output.append(sub[:])
            
            for x in range(i, len(nums)):
                if x > i and nums[x] == nums[x-1]:
                    continue
                
                sub.append(nums[x])
                backtrack(x + 1)
                sub.pop()
        backtrack(0)
        return output