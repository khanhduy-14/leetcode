class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        can_group = 1

        for i in range(len(s)):
            char = s[i]
            prev_char = s[i-1] if i > 0 else ''
            prev_res = res
            
            if int(char) >= 1 and int(char) <=26:
                if int(prev_char+char) >= 1 and int(prev_char+char) <=26:
                    res+=can_group
                    can_group = prev_res if i > 0 else 1
                else: 
                    can_group = res
            else:
                if int(prev_char+char) >= 1 and int(prev_char+char) <=26:
                    res=can_group if i > 0 else 0
                else:
                    res = 0
                can_group = 0
          
        return res