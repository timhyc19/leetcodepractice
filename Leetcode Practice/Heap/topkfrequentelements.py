import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        heap = []
        for val in nums:
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1

        # time complexity is O(n*logk)
        for key, val in counts.items():
            # Constantly push key and value (number and frequency)
            heapq.heappush(heap, (val, key))

            if(len(heap) > k):
                # if the length of the heap is greater than limit, remove smallest (heap pop)
                heapq.heappop(heap)

        return [k for v, k in heap]