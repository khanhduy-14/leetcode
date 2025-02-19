class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        valid_chars = 'abc'
        happy_strings = []
        def backtracking(string):
            if len(string) == n:
                happy_strings.append(string)
                return 
            for i in range(len(valid_chars)):
                prev_char = string[-1] if len(string) > 0 else None
                if prev_char and prev_char == valid_chars[i]:
                    continue
                else:
                    backtracking(string+valid_chars[i])
        backtracking('')
        return happy_strings[k-1] if 0 <= k-1 < len(happy_strings) else ''


        