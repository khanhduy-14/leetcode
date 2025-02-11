class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        

        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= len(part) and "".join(stack[len(stack) - len(part):]) == part:
                stack = stack[0: len(stack) - len(part)]
            

        return "".join(stack)

        