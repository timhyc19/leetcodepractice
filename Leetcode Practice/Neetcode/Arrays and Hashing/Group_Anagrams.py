class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for char in strs:
            characters = [0] * 26
            for c in char:
                characters[ord('a') - ord(c)] += 1
            d[tuple(characters)].append(char)
        
        return d.values()
