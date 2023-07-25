class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        count = n - 1
        for c in reversed(s):
            for val in wordDict:
                if val == s[count:count + len(val)]:
                    dp[count] = dp[count + len(val)]
                if dp[count]:
                    break
            count -= 1

        return dp[0]
