class Solution:
    def calculateDistance(self, x, y):
        return math.sqrt(x**2  + y**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # (distance, point)
        heapq.heapify(heap)
        for point in points:
            d = -self.calculateDistance(point[0], point[1])
            heapq.heappush(heap, [d, point])
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [x[1] for x in heap]
    