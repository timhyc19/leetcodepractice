class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxRate = max(piles)
        minRes = maxRate
        l, r = 1, maxRate
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
            
            if hours <= h:
                r = m - 1
                minRes = min(minRes, m)
            else:
                l = m + 1

        return minRes
    