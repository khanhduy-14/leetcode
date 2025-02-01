class Solution:
    def partition(self, s: str) -> List[List[str]]:

        substring = ''
        result = []
        def is_palindrome(str):
            for i in range(0, int(len(str)/2)):
                if str[i] != str[len(str)-i-1]:
                    return False
            return True

        def backtrack(start, substrings):
            if start == len(s):
                result.append(substrings)
                return

            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    backtrack(end, substrings + [s[start:end]])

        backtrack(0,[])
        return result
      

        