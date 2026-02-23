class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substr = set()
        n = len(s)
        for i in range(0, n - k + 1):
            substr.add(s[i: i+k])
        
        return len(substr) == 2**k