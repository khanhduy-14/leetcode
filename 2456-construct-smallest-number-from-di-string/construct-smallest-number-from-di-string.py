class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        res = ""
        for i in range(1, len(pattern) + 2):
            stack.append(i)

            while stack and (i == len(pattern) + 1 or pattern[i-1] == 'I'):
                res+=str(stack.pop())
                
        return res
                

            

            
        