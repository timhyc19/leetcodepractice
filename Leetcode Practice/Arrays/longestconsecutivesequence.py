class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = set(nums)
        maxLength = 0
        for num in nums:
            if (num-1) not in d:
                curr = 1
                while (num + curr) in d:
                    curr += 1
                maxLength = max(maxLength, curr)
        
        return maxLength
    