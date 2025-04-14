class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(arr)
        MAX_VALUE = 1000
        prefix_counts = [0] * (MAX_VALUE + 1)

        for j in range(n):
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) > b:
                    continue

                lower = max(0, arr[j] - a, arr[k] - c)
                upper = min(MAX_VALUE, arr[j] + a, arr[k] + c)

                if lower > upper:
                    continue

                if lower == 0:
                    valid = prefix_counts[upper]
                else:
                    valid = prefix_counts[upper] - prefix_counts[lower - 1]

                count += valid

            # Update prefix_counts for future queries
            for x in range(arr[j], MAX_VALUE + 1):
                prefix_counts[x] += 1

        return count