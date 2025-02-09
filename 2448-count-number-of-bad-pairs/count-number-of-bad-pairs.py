class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = {} 
        total_pairs = (len(nums) * (len(nums) -1 )) / 2
        total_good_pairs = 0
        for i in range(len(nums)):
                key = nums[i] - i
                total_good_pairs+= freq.get(key,0)
                freq[key] = freq.get(key, 0) + 1
        print(total_pairs, total_good_pairs)
        n = len(nums)
        print(n)
        return int(total_pairs - total_good_pairs)
 
        