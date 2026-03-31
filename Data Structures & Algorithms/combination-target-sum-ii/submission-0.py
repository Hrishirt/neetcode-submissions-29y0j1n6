class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 
        
        output = []
        sums = [] 

        def backtrack(i, val): 
            if val == target: 
                output.append(sums[:])
                return 
            
            if val > target or i >= len(candidates): 
                return 
            
            for x in range(i, len(candidates)):
                if x > i and candidates[x] == candidates[x-1]: 
                    continue 
                sums.append(candidates[x])
                print(sums)
                backtrack(x + 1, val + candidates[x])
                sums.pop() 
            
        backtrack(0,0)
        return output

