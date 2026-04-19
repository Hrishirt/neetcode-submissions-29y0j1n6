class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        heap = []
        output = []
        for num, freq in hashmap.items():
            heapq.heappush(heap, (freq, num))
        
        while len(heap) > k: 
            heapq.heappop(heap)
        
        while len(heap) != 0: 
            output.append(heapq.heappop(heap)[1])
        
        return output