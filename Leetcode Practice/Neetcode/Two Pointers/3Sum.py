class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            curr = nums[i]
            if curr > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums)-1
            while l < r:
                s = curr + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res
