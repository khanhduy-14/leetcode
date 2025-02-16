class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        check = 0
        for i in range(len(s) - k + 1):
            beforeChar = s[i - 1] if i-1 >=0 else None
            if beforeChar and beforeChar == s[i]:
                check=0
                continue
            afterChar = s[i + k] if i+k< len(s) else None
            if afterChar and afterChar == s[i]:
                check=0
                continue
            char = s[i]
            check = 1
            for i in range(i+1, i+k):
                print(s[i], char)
                if s[i] == char:
                    check+=1
            if check == k:
                return True
            else:
                check=0
                continue
        return False
        