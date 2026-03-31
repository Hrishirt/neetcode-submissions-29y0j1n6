class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        freq = [[] for x in range (len(nums) + 1 )]
        res = [] 

        for c in nums:
            cnt[c] = 1 + cnt.get(c, 0)
        for x, y in cnt.items():
            freq[y].append(x)
        
        for x in reversed(freq):
            for c in x:
                res.append(c)
                if len(res) == k:
                    return res