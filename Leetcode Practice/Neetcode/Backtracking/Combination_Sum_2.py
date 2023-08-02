class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # 1, 1, 2, 5, 6, 7, 10

        res = []

        def dfs(index, total, arr):
            if total == target:
                res.append(arr.copy())
                return
            elif total > target or index >= len(candidates):
                return
            else:
                # choose the current value
                arr.append(candidates[index])
                dfs(index + 1, total + candidates[index], arr)

                # do not choose the current value, and keep going
                arr.pop()
                while (index + 1) < len(candidates) and candidates[index] == candidates[index + 1]:
                    index += 1
                dfs(index + 1, total, arr)
        
        dfs(0, 0, [])
        return res
    