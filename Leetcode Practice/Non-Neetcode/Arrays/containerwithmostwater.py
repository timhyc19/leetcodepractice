class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # two pointer approach
        l = 0
        r = len(height) - 1
        maxArea = 0
        while l <= r:
            # current max area is length * min(heights)
            currArea = (r - l) * min(height[l], height[r])

            # reset maxArea if necessary
            if(currArea >= maxArea):
                maxArea = currArea

            # adjust pointers    
            if(height[l] < height[r]):
                l += 1
            else:
                r -= 1
        
        return maxArea