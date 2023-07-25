class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minVal = prices[0]
        maxVal = 0
        for price in prices:
            minVal = min(minVal, price)
            maxVal = max(maxVal, price - minVal)
        
        return maxVal