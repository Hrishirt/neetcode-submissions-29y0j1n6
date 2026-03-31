class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = [] 
        combs = [] 
        def backtrack(i):
            if len(combs) == k:
                output.append(combs[:])
                return 
            
            for num in range(i, n + 1):
                combs.append(num)
                backtrack(num + 1)
                combs.pop()
        backtrack(1)
        return output