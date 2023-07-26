import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = Counter(tasks)
        heap = [-t for t in t.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0

        while heap or q:
            time += 1
            if heap:
                count = heapq.heappop(heap) + 1
                if count != 0:
                    q.append([count, time + n])
                

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time

