class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        Recognize that it is fibonnaci
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            dp = [1] * (n)
            print(dp)
            dp[1] = 2
            dp[2] = 3
            for i in range(2, n):
                print(i)
                dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]