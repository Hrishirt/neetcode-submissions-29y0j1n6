class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {} 

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for j in range(len(s)):
            if countS[s[j]] == countT.get(s[j], 0):
                continue
            else:
                return False
        return True