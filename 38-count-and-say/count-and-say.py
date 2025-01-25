class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n <= 1:
            return str(n)
        
        rleStore = ['1']

        for i in range(1,n):
            print(rleStore)
            groupCount = self.groupIdentical(rleStore[i-1])
            rleStore.append(''.join(str(num) + char for num, char in groupCount))
        return rleStore[len(rleStore) - 1]


    def groupIdentical(self, s: str) -> list[list[str]]:
        character = s[0]
        freq = 1
        groupCount = []
        for i in range(1, len(s)):
            if s[i] == character:
                freq+=1
            else:
                groupCount.append([freq, character])
                character = s[i]
                freq = 1
        groupCount.append([freq, character])
        return groupCount