import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        # initialize heap of size 0 to k (this is going to be the limited size of our heap)
        self.n = len(nums)
        self.k = k
        self.heap = nums[:min(k, self.n)]
        print(self.heap)

        # heapify     
        heapq.heapify(self.heap)


        # for every subsequent value, push and pop the smallest value between nums[i] and min(self.heap)
        for i in range(k, self.n):
            # note: below is faster than heap push, then pop
            heapq.heappushpop(self.heap, nums[i])


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)