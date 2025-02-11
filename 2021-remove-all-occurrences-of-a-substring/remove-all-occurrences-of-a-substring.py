class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = ""
        

        for i in range(len(s)):
            stack+=s[i]
            if stack[len(stack) - len(part):] == part:
                stack = stack[:len(stack) - len(part)]

        return stack

        