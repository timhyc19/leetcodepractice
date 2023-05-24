import heapq


class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums1)
        # useful function: zip
        pairs = list(sorted(zip(nums2, nums1), reverse=True))
        s = 0
        r = 0
        heap = []
        # [(4, 2), (3, 3), (2, 1), (1, 3)]

        # the values in the same index of nums1 and nums2 will "travel" together, because it is grouped as a pair
        for minNum, maxNum in pairs:
            # push the curr "max" value into the heap, add it to our cumulating sum
            heapq.heappush(heap, maxNum)
            s += maxNum

            # if we get overflow above size k, we need to remove the smallest element, which is at the top of the heap,
            # and also remove it from the sum
            if len(heap) > k:
                s -= heapq.heappop(heap)

            # whenever the length of the heap is equal to the size, we need to update our return value
            # simply the max of its possible previous value, as well as the iterating minNum * sum (s)
            if len(heap) == k:
                r = max(r, minNum * s)

        return r