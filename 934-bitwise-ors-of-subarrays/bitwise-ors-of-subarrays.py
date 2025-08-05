class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        curr, seen = set(), set()

        for num in arr:
            next_curr = set([num])
            for val in curr:
                next_curr.add(val | num)

            curr=next_curr
            seen.update(curr)
        
        return len(seen)