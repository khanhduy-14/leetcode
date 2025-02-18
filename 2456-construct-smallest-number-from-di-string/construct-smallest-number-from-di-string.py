class Solution:
    def smallestNumber(self, pattern: str) -> str:
        valid_nums = []
        used_nums= set()
        def backtracking(string: str, min: int, max: int) -> str:
            if len(string) == len(pattern) + 1:
                valid_nums.append(int(string))
            for i in range(1, len(pattern)+2):
                if i not in used_nums and i > min and i < max:
                    used_nums.add(i)
                    if len(string) == len(pattern):
                        valid_nums.append(int(string + str(i)))
                    else:
                        backtracking(string+str(i), 0 if pattern[len(string)] == 'D' else i,i if  pattern[len(string)] == 'D' else len(pattern)+2)
                    used_nums.remove(i)
                else:
                    continue;
        backtracking('', 0, len(pattern) + 2)
        return str(min(valid_nums))
                

            

            
        