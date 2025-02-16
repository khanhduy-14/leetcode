class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        days = len(pizzas) // 4
        pizzas.sort()
        max_sum = 0
        oddDays = (days + 1) // 2
        evenDays = days // 2
        for i in range(oddDays):
            max_sum+=pizzas.pop()
        for i in range(evenDays):
            pizzas.pop()
            max_sum+=pizzas.pop()
            
        return max_sum
            