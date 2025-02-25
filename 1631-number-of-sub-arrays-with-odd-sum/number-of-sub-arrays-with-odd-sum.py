class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
      res, curr_sum, even_sum, odd_sum = 0, 0, 1, 0
      

      for num in arr:
        curr_sum+=num
        if curr_sum % 2 == 1:
            odd_sum +=1
            res+=even_sum
        else:
            even_sum+=1
            res+=odd_sum
    
      return res % (pow(10,9) + 7)