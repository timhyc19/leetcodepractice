class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #O(log n) requires binary search
        l = 0
        r = len(nums) - 1
        while(l <= r):
            mid = (r+l)/2
            if(nums[mid] == target):
                return mid
            
            # left is sorted
            if(nums[l] <= nums[mid]):
                # target in between
                if(nums[l] <= target and nums[mid] >= target):
                    r = mid - 1
                else:
                    l = mid + 1

            # else right is sorted
            else:
                if(target <= nums[r] and nums[mid] <= target):
                    l = mid + 1
                else:
                    r = mid - 1
            
        return -1