class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        left, right, res = 0,0,0
        colors.extend(colors[:k-1])

        for right in range(len(colors)):
            if right > 0 and colors[right] == colors[right-1]:
                left = right
                if left > (len(colors) - 1):
                    break
            if right - left + 1 >= k:
                res+=1
            
        return res
            
        
     