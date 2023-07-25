class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        comp = [0] * 26
        for i in range(len(s1)):
            comp[ord('a') - ord(s1[i])] += 1

        while r <= len(s2) - 1:
            arr = [0] * 26
            for i in range(len(s1)):
                arr[ord('a') - ord(s2[l+i])] += 1
            
            if arr == comp:
                return True
            l += 1
            r += 1
        
        return False
