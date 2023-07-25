class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        minVal = 0
        if(len(nums) == 1):
            return nums[0]

        while(l <= r):
            m = (l + r)/2
            if nums[l] < nums[r]:
                return nums[0]
            
            if(nums[m+1] < nums[m]):
                return nums[m+1]
            
            if(nums[m] < nums[m-1] and nums[m] < nums[m+1]):
                return nums[m]
        
            if nums[l] < nums[m] and nums[m] > nums[r]:
                l = m + 1
            elif nums[l] > nums[m] and nums[m] < nums[r]:
                r = m - 1