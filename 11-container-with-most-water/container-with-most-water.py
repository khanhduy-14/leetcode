class Solution:
    def maxArea(self, height: List[int]) -> int:
        mArea = 0
        lIndex = 0
        rIndex = len(height) - 1;
        while lIndex < rIndex: 
            sArea = min(height[lIndex],height[rIndex]) * (rIndex - lIndex)
            if sArea > mArea:
                mArea = sArea
            if height[lIndex] > height[rIndex]:
                rIndex-=1
            else:
                lIndex+=1

        return mArea
        