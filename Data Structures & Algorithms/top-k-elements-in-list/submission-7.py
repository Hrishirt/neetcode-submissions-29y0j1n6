class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {} 
        res = [[] for _ in range(len(nums) + 1)]
        output = []
        for num in nums:
            cnt[num] = 1 + cnt.get(num,0)
        
        for key, val in cnt.items():
            res[val].append(key)
        
        for x in reversed(res):
            for y in x: 
                output.append(y)
                if len(output) == k:
                    return output