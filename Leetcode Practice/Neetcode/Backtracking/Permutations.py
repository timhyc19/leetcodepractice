class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(arr):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            else:
                for i in range(len(nums)):
                    if nums[i] not in arr:
                        arr.append(nums[i])
                        dfs(arr)
                        arr.pop()
        
        dfs([])
        return res
    