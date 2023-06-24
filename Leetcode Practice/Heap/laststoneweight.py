import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            valOne = heapq.heappop(stones)
            valTwo = heapq.heappop(stones)
            if valOne > valTwo:
                heapq.heappush(stones, valTwo - valOne)
            elif valTwo > valOne:
                heapq.heappush(stones, valOne - valTwo)

        if len(stones) == 0:
            return 0
        return -stones[0]
    