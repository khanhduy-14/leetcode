class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        if x < y:
            return self.remove_substrings(s, "ba", y, "ab", x)
        else:
            return self.remove_substrings(s, "ab", x, "ba", y)

    def remove_substrings(self, s: str, first: str, x: int, second: str, y: int) -> int:
        stack = []
        score = 0
        for c in s:
            if stack and stack[-1] == first[0] and c == first[1]:
                stack.pop()
                score += x
            else:
                stack.append(c)
        s2 = "".join(stack)
        
        stack = []
        for c in s2:
            if stack and stack[-1] == second[0] and c == second[1]:
                stack.pop()
                score += y
            else:
                stack.append(c)
        
        return score