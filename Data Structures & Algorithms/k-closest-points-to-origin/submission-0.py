class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        output = []
        for point in points: 
            heapq.heappush(min_heap, (point[0]**2 + point[1]**2, point[0], point[1]))
        

        while len(output) < k: 
            distance = heapq.heappop(min_heap)
            output.append([distance[1], distance[2]])
        return output
