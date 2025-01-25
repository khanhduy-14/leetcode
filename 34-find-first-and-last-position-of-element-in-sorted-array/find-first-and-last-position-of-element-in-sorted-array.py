class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        minIndex = -1
        maxIndex = -1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                minIndex = mid
                maxIndex = mid
                break;
            if nums[mid] > target:
               right = mid - 1
            else:
                left = mid + 1

        if minIndex > -1:
            while minIndex > 0 and nums[minIndex-1] == target:
                minIndex-=1
            while maxIndex < len(nums) -1 and nums[maxIndex+1] == target:
                maxIndex+=1
        
       
        return [minIndex, maxIndex]