class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        res = 0
        for val in prices:
            minPrice = min(minPrice, val)
            res = max(res, val - minPrice)
        
        return res
    