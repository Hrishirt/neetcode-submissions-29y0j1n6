class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1counter = Counter(s1)
        s2counter = Counter(s2[:len(s1)])
        for x in range(len(s2) - len(s1)): 
            if s1counter == s2counter:
                return True 
            s2counter[s2[x + len(s1)]] += 1
            left = s2[x]
            s2counter[left] -= 1
            if s2counter[left] == 0: 
                del s2counter[left]
        return s2counter == s1counter