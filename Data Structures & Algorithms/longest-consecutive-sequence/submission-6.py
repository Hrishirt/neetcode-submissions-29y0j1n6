class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        for num in nums: 
            if num-1 in nums: 
                continue
            else:
                length = 1
                temp = num + 1 
                while temp in nums: 
                    length += 1
                    temp += 1 
                longest = max(longest, length)
        return longest