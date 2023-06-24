import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def distance(x1, y1):
            return math.sqrt((x1)**2 + (y1)**2)

        heap = []
        for id, p in enumerate(points):
            d = distance(p[0], p[1])
            if len(heap) < k:
                heapq.heappush(heap, (-d, id))
            else:
                heapq.heappushpop(heap, (-d, id))
            

        return [points[id] for _, id in heap]
    