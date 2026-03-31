class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''
        for char in s:
            if char.isalnum():
                s2 += char.lower()
        if s2 == s2[::-1]:
            return True
        else:
            return False