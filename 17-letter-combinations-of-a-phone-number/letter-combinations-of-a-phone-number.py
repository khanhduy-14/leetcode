class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxzy",
        }
        if not digits:
            return []
        
        res = []
        def backtrack(curr, i):
            if len(curr) == len(digits):
                res.append(curr)
                return
            for char in digit_to_char[digits[i]]:
                backtrack(curr + char, i+1)



        backtrack('', 0)

        return res
