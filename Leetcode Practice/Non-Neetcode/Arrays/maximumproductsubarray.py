class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minProduct = 1
        maxProduct = 1
        r = float('-inf')
        for val in nums:
            if val < 0:
                temp = minProduct
                minProduct = maxProduct
                maxProduct = temp
            
            maxProduct = max(maxProduct * val, val)
            minProduct = min(minProduct * val, val)

            r = max(r, maxProduct)
        
        return r