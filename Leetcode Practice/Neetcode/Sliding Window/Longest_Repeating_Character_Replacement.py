class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        d = {}
        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r], 0)
            m = max(d.values())
            if (r - l + 1) - m > k:
                d[s[l]] -= 1
                l += 1
        
        return (r - l + 1)

