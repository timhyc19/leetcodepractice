class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        tmpArr = [1] * n
        multiplier_left = nums[0]
        for i in range(1, n):
            tmpArr[i] = multiplier_left
            multiplier_left *= nums[i]
    
        multiplier_right = nums[n-1]
        for i in range(2, n+1):
            tmpArr[n-i] *= multiplier_right
            multiplier_right *= nums[n-i]
        
        return tmpArr