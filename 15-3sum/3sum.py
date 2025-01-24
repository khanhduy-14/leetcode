class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1 
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1

                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
                elif sum > 0:
                    k-=1
                else:
                    j+=1
        
        return result