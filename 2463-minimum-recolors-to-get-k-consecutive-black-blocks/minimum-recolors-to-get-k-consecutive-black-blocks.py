class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curr = 0
        for i in range(k):
            if blocks[i] == 'W':
                curr+=1
        res = curr
        for i in range(k, len(blocks)):
            if blocks[i-k] == 'W':
                curr-=1
            if blocks[i] == 'W':
                curr+=1
            res = min(curr, res)
        return res
                
                

        