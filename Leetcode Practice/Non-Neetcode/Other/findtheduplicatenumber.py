class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            i = abs(num)
            if nums[i] < 0:
                return i
            nums[i] = -nums[i]
        

        