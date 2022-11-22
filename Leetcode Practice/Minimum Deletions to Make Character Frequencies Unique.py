class Solution:
    def minDeletions(self, s: str) -> int:
        dictionary = {}
        returnVal = 0
        uniqueList = set()

        for val in s:
            if val in dictionary:
                dictionary[val] += 1
            else:
                dictionary[val] = 1

        for key, value in dictionary.items():
            while value > 0 and value in uniqueList:
                value -= 1
                returnVal += 1
            
            uniqueList.add(value)
        
        return returnVal