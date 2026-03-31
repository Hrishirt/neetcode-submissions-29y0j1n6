class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  
        found = False
        while not found:
            currSum = numbers[l] + numbers[r]

            if currSum > target:
                r -= 1 
            elif currSum < target:
                l += 1 
            else:
                found = True
                return [l +1, r+1]
        return []