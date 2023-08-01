class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, total, arr):
            if total == target:
                res.append(arr.copy())
                return
            elif total >= target or index >= len(candidates):
                return
            else:
                arr.append(candidates[index])
                dfs(index, total + candidates[index], arr)
                arr.pop()
                dfs(index + 1, total, arr)
    
        dfs(0, 0, [])
        return res

