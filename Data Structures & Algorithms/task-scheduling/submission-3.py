class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = Counter(tasks)
        maxHeap = []
        for val in hashmap.values(): 
            heapq.heappush(maxHeap, -val)
        
        time = 0 
        q = deque() 
        while len(maxHeap) != 0 or len(q) != 0: 
            time += 1 
            if len(maxHeap) > 0: 
                cnt = heapq.heappop(maxHeap) + 1 
                print(cnt)
                if cnt != 0: 
                    q.append([cnt, n + time])
            if len(q) > 0 and time == q[0][1]: 
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time 
