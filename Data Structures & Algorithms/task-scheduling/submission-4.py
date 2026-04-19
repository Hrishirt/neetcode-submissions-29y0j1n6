class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = Counter(tasks)
        time = 0 
        heap = [] 
        for x in hashmap.values():
            heapq.heappush(heap, -x)
        
        q = deque() 
        while len(heap) > 0 or len(q) > 0: 
            time += 1 
            if len(heap) > 0:
                cnt = heapq.heappop(heap) + 1 
                if cnt < 0: 
                    q.append([cnt, time + n])
            if len(q) > 0 and q[0][1] == time: 
                poppedVal = q.popleft()[0]
                heapq.heappush(heap, poppedVal)
        return time