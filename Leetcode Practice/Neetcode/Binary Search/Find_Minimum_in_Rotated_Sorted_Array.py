class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1, 2, 3, 4, 5]
        # [3, 4, 5, 1, 2]  --> [1, 2] --> [1]
        # [6, 1, 2, 3, 4] --> [6, 1]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[l]:
                r = m
            else:
                return nums[l]
            