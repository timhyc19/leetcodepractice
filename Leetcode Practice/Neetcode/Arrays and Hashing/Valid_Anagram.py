class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1, c2 = Counter(s), Counter(t)
        if c1 == c2: return True
        return False
    