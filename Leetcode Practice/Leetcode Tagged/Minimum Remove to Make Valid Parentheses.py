class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        exclude = set()
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append((s[i], i))
            elif s[i] == ")":
                if len(stack) > 0 and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((s[i], i))
        
        for element in stack:
            exclude.add(element[1])
        
        res = ""
        for i in range(len(s)):
            if i not in exclude:
                res += s[i]

        return res