class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i].isdigit():
                s_list[stack.pop()] = ''
                s_list[i] = ''
            
            else:
                stack.append(i)
        
        return ''.join(s_list)
        