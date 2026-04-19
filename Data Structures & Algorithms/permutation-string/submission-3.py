class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1counter = Counter(s1)
        right = Counter(s2[:len(s1)])
        
        for s in range(len(s2) - len(s1)):
            if right == s1counter:
                return True
            
            right[s2[s + len(s1)]] += 1 
            left = s2[s]
            right[s2[s]] -= 1 
            if right[left] == 0:
                del right[left]
        
        if s1counter == right:
            return True
        else:
            return False