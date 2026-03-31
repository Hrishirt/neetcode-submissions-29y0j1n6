class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r 
        '''
        ks = []
        for i in range(r +1):
            ks.append(i)
        '''
        while l <= r:
            k = (r + l) // 2 
            time = 0 
            for x in piles:
                time += math.ceil(float(x)/k)
            
            if time > h: 
                l = k + 1 
            else:
                res = k
                r = k -1 
        return res