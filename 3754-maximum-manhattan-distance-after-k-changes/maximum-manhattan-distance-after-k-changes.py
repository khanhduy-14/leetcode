class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        ans = 0
        for c in s:
            freq[c] += 1
            num_of_opposite_dirs = min(freq["N"], freq["S"]) + min(freq["W"], freq["E"])
            
            man_dis= sum(freq.values()) - (2 * num_of_opposite_dirs)

            man_dis+= (2 * min(k, num_of_opposite_dirs))
            ans = max(ans, man_dis)
                
        return ans