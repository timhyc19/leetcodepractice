class MedianFinder:

    def __init__(self):
        self.leftHeap = [] # maxHeap
        self.rightHeap = [] # minHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftHeap, -num)
        if self.leftHeap and self.rightHeap and self.rightHeap[0] < -self.leftHeap[0]:
            popVal = -heapq.heappop(self.leftHeap) 
            heapq.heappush(self.rightHeap, popVal)
        

        if len(self.leftHeap) > len(self.rightHeap) + 1:
            popVal = -heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, popVal)
        
        if len(self.leftHeap) + 1 < len(self.rightHeap):
            popVal = heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, -popVal) 
    
        


    def findMedian(self) -> float:
        if len(self.leftHeap) > len(self.rightHeap):
            return -self.leftHeap[0]
        elif len(self.leftHeap) < len(self.rightHeap):
            return self.rightHeap[0]
        else:
            return (-self.leftHeap[0] + self.rightHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
