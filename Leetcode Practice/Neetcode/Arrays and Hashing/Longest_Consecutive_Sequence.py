class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for val in nums:
            length = 0
            if (val - 1) not in s:
                while (val + length) in s:
                    length += 1
            
            res = max(res, length)
        
        return res
        
        