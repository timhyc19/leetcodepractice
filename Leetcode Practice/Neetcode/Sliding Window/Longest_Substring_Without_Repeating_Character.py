class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0
        for r in range(len(s)):
            c = s[r]
            while c in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(c)
            res = max(res, len(charSet))
        
        return res
