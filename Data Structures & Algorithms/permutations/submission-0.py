class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        perms = [] 

        def backtrack():
            if len(perms) == len(nums): 
                output.append(perms[:])
                return 
            
            for num in nums: 
                if num in perms:
                    continue 
                perms.append(num)
                backtrack() 
                perms.pop() 

        backtrack() 
        return output