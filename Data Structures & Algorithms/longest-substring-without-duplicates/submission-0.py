class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = set()
        length = 0 
        l = 0
        for r in range(len(s)):
            while s[r] in checker: 
                checker.remove(s[l])
                l += 1 
            checker.add(s[r])
            length = max(length, r - l + 1)
        return length
        
        