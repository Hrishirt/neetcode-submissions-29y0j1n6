class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorteds1 = sorted(s1)
        sorteds1 = ''.join(sorteds1)
        for x in range(len(s2) - len(s1) + 1):
            if ''.join(sorted(s2[x:x+len(sorteds1)])) == sorteds1:
                return True 
        return False