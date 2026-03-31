class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for index, number in enumerate(nums):
            if target - number in tracker:
                return [tracker[target - number], index]
            else:
                tracker[number] = index 
