class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = Counter(tiles)
        def backtracking():
            res = 0
            for char in freq:
                if freq[char] > 0:
                    freq[char]-=1
                    res+=1
                    res+=backtracking()
                    freq[char]+=1
            return res
        
        return backtracking()
