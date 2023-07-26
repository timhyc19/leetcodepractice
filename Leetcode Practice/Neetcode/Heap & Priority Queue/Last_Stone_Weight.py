class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            v1 = heapq.heappop(heap)
            v2 = heapq.heappop(heap)
            newVal = v1 - v2
            heapq.heappush(heap, newVal)
        
        return -heap[0]
    