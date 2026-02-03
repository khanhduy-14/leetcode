class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p1 = 0
       
        for i  in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                p1 = i
            elif nums[i] == nums[i-1]:
                return False
            else:
                break
        q = p1+1
        for i  in range(p1+2, len(nums)):
            if nums[i] < nums[i-1]:
                q = i
            elif nums[i] == nums[i-1]:
                return False
            else:
                break
        p2= q+1
        for i  in range(q+2, len(nums)):
            if nums[i] > nums[i-1]:
                p2=i
            elif nums[i] == nums[i-1]:
                return False
            else:
                break
        print("p1: " + str(p1) + " q: " + str(q) + " p2: " + str(p2))
        return p1 > 0 & p1 < q & q < p2  & p2 == len(nums) -1
        