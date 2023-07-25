class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers)-1
        while l < r:
            diff_left = target - numbers[l]
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            if diff_left < numbers[r]:
                r -= 1
            else:
                l += 1
                