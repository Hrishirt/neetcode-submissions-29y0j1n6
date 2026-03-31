class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {} 
        
        if len(s) != len(t):
            return False
        
        for v in range(len(s)):
            countS[s[v]] = 1 + countS.get(s[v], 0)
            countT[t[v]] = 1 + countT.get(t[v], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True