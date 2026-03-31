class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''
        for char in s:
            if char.isalnum():
                s2 += char.lower()
        l = 0 
        r = len(s2) - 1
        while l < r:
            if s2[l] == s2[r]:
                l += 1 
                r -= 1 
            else:
                return False
        return True 