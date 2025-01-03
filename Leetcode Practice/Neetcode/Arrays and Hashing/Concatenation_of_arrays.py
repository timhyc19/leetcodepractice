"""
Initial thought process is to create the new array of size 2*len(nums). 
To track indices efficiently, use the modulo operation
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        n = 2 * len(nums)
        for i in range(n):
            res.append(nums[i % len(nums)])
        return res