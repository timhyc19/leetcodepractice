class Solution(object):
    def isValid(self, c):
        return (ord("A") <= ord(c) <= ord("Z")
                or ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9")
                )
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s)-1
        s = s.lower()
        while l < r:
            while l < r and not self.isValid(s[l]):
                l += 1
            while l < r and not self.isValid(s[r]):
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
            
        return True
    