class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        energy = 0

        for power in nums:
            if energy < 0:
                return False
            elif power > energy:
                energy = power
            
            energy-=1
        
        return True

        