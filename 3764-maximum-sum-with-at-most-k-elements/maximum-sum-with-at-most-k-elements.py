class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        sum = 0
        selected_nums = []
        if k <= 0:
            return 0
        for i in range(len(grid)):
            limit = limits[i]
            pick_limit_nums = []
            for j in range(len(grid[i])):
                    if len(pick_limit_nums) < limit:
                        heapq.heappush(pick_limit_nums, grid[i][j])
                    else:
                        heapq.heappushpop(pick_limit_nums, grid[i][j])
            selected_nums+=pick_limit_nums
        selected_nums = [-num for num in selected_nums]
        heapq.heapify(selected_nums)
        while k > 0: 
            sum+=(heapq.heappop(selected_nums)*-1)
            k-=1
            
        return sum
                        
                        
                        
                        
            
        
        