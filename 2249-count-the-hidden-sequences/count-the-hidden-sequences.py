class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        curr = 0
        min_pref = 0
        max_pref = 0

        # Compute running prefix sum and track min/max
        for d in differences:
            curr += d
            min_pref = min(min_pref, curr)
            max_pref = max(max_pref, curr)

        # The span of values the array can take due to differences
        span = max_pref - min_pref
        shift_capacity = upper - lower

        # Total valid initial values that keep the array within bounds
        return max(0, shift_capacity - span + 1)