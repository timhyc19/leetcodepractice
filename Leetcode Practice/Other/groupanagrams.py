import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        for val in strs:
            count = [0] * 26
            for c in val:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(val)
        
        return res.values()
    