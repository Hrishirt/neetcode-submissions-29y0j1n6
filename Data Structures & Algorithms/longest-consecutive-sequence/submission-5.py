class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        nums = set(nums)
        for x in nums:
            if x - 1 not in nums:
                length = 1
                temp = x + 1 
                while temp in nums:
                    length += 1 
                    temp += 1 
                longest = max(length, longest)
        return longest