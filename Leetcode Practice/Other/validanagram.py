class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        if n != len(t):
            return False
        
        s_d = {}
        t_d = {}
        for i in range(n):
            s_d[s[i]] = 1 + s_d.get(s[i], 0)
            t_d[t[i]] = 1 + t_d.get(t[i], 0)
        
        return s_d == t_d
    