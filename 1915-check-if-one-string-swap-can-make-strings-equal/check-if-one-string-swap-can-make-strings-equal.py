class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = 0
        freq1 = Counter(s1)
        freq2 = Counter(s2)
        if freq1 != freq2:
            return False
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff+=1

            if diff > 2:
                return False
        return diff == 2 or diff == 0