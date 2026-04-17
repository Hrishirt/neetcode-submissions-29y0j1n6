class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for val in stones:
            heapq.heappush(max_heap, -val)

        while len(max_heap) > 1: 
            x = -1 * heapq.heappop(max_heap)
            y = -1 * heapq.heappop(max_heap)
            if x == y: 
                continue
            elif y < x: 
                heapq.heappush(max_heap, -1*(x - y))

        
        if len(max_heap) == 0:
            print(max_heap)
            return 0
        else:
            print(max_heap)
            return -max_heap[0]