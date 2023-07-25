import collections

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dictCounts = collections.Counter(nums)
        sumCount = 0
        for val in dictCounts.values():
            sumCount += (val * (val - 1) // 2)
            
        return sumCount
    
    