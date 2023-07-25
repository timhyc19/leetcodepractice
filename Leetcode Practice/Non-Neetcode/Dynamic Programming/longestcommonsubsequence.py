class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # lcs = {}
        #
        # def solve(i, j):
        #     if i < 0 or j < 0:
        #         return 0
        #
        #     if (i, j) in lcs:
        #         return lcs[(i, j)]
        #     if text1[i] == text2[j]:
        #         lcs[(i, j)] = 1 + solve(i - 1, j - 1)
        #     else:
        #         lcs[(i, j)] = max(solve(i - 1, j), solve(i, j - 1))
        #
        #     return lcs[(i, j)]
        #
        # return solve(len(text1) - 1, len(text2) - 1)
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        r = 0
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max((dp[i][j - 1]), (dp[i - 1][j]))
                r = max(r, dp[i][j])

        return r
