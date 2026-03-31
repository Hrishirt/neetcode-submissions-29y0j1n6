class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = {} 

        for index, number in enumerate(numbers):
            if target - number in nums:
                return [nums[target - number], index + 1]
            else:
                nums[number] = index + 1 