class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * ((n*2) -1)
        usedSet = {}
        def backtrack(startIndex: int):
            if startIndex == len(res):
                return True
            if res[startIndex]:
                return backtrack(startIndex+1)

            for num in range(n, 0, -1):
                if num in usedSet:
                    continue
                nextIndex = startIndex + num if num > 1 else startIndex
           
                if nextIndex >= len(res):
                    continue
                if res[startIndex] == 0 and res[nextIndex] == 0:
                    res[startIndex] =  num
                    res[nextIndex] = num
                    usedSet[num] = True
                    print(backtrack(startIndex+1))
                    if backtrack(startIndex+1):
                        return True
                    res[startIndex]= 0
                    res[nextIndex] = 0
                    del usedSet[num]
                else:
                    continue
            return False
                
        backtrack(0)
        return res