class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        if k == 0:
            return 1.0
        dp = [0.0] * (n+1)
        dp[0] = 1.0
        s = 1.0
        for i in range(1, n+1):
            dp[i] = s * 1/maxPts
            
            if i < k:
                s += dp[i]
           
            if i - maxPts >= 0 and i - maxPts < k:
                s -= dp[i-maxPts]
        
        return sum(dp[k:])
    