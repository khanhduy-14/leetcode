class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        first = -1
        last = -1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                first = mid
                last = mid
                break;
            if nums[mid] > target:
               right = mid - 1
            else:
                left = mid + 1

        if first > -1:
            while first > 0 and nums[first-1] == target:
                first-=1
            while last < len(nums) -1 and nums[last+1] == target:
                last+=1
        
       
        return [first, last]