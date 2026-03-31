class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {} 
        freq = [[] for i in range(len(nums) + 1)]
        res = [] 
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
        for n, c in cnt.items():
            freq[c].append(n)
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res