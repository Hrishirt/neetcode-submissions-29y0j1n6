class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = Counter(tasks)
        max_heap = []
        for num in hashmap.values():
            heapq.heappush(max_heap, -num)

        q = deque() 
        time = 0
        while len(max_heap) != 0 or len(q) != 0: 
            time += 1 

            if len(max_heap) != 0: 
                cnt = heapq.heappop(max_heap) + 1 
                if cnt != 0: 
                    q.append([cnt, time + n])
            
            if len(q) != 0 and q[0][1] == time: 
                heapq.heappush(max_heap, q.popleft()[0])
        return time 
