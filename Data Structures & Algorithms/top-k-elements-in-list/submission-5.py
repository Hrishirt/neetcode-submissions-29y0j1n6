class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        freq = [[] for _ in range(len(nums) + 1)]
        res = [] 
        for x in nums:
            cnt[x] = 1 + cnt.get(x, 0)
        
        for c, n in cnt.items():
            freq[n].append(c)
        
        for i in reversed(range(len(freq))):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res