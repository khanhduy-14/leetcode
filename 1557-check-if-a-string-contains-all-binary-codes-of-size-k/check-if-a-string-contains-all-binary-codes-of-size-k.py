class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        n = len(s)
        for i in range(0, n - k + 1):
            seen.add(s[i: i+k])
        
        return len(seen) == 2**k