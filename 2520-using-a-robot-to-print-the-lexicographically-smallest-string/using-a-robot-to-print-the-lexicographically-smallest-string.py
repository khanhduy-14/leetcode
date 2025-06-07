class Solution:

    def buildMinArr(self,s: str) -> list[int]:
        n = len(s)
        arr = [''] * n
        arr[n-1]= s[n-1]
        for i in range(n-2, -1,-1):
            arr[i] =  min(s[i], arr[i+1])
        return arr
        
    def robotWithString(self, s: str) -> str:
        min_arr = self.buildMinArr(s)
        stack = []
        n = len(s)
        res = ''
        for i in range(len(s)):
            stack.append(s[i])
            while stack and (i == n-1 or stack[-1] <= min_arr[i+1]):
                res+=stack.pop()
        return res
        
        