class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l <= r:
            s = numbers[r] + numbers[l]
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return [l+1, r+1]
            