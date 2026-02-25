class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        buckets = [[] for _ in range(14)]

        for num in arr:
            buckets[num.bit_count()].append(num) 
        
        for bucket in buckets:
            bucket.sort()
        
        res = []

        for bucket in buckets:
            res.extend(bucket)
        
        return res