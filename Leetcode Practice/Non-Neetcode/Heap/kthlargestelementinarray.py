import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        heapq.heapify(heap)
        for val in nums:
            if len(heap) < k:
                heapq.heappush(heap, val)
            else:
                heapq.heappushpop(heap, val)
        
        return heapq.heappop(heap)
    