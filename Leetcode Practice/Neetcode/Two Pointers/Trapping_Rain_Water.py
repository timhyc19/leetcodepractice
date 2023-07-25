class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftHeight, rightHeight = height[l], height[r]
        res = 0
        while l < r:
            if leftHeight < rightHeight:
                l += 1
                leftHeight = max(leftHeight, height[l])
                res += leftHeight - height[l]
            else:
                r -= 1
                rightHeight = max(rightHeight, height[r])
                res += rightHeight - height[r]
        
        return res

            