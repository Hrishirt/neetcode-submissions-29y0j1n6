class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {} 

        if len(s) != len(t):
            return False
        for u in range(len(s)):
            countS[s[u]] = 1 + countS.get(s[u], 0)
            countT[t[u]] = 1 + countT.get(t[u], 0)
        
        for x in countS:
            if countS[x] != countT.get(x, 0):
                return False
        return True