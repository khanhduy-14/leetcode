
class NumberContainers:

    def __init__(self):
        self.numberListIndexMap = {}
        self.indexCurrentNumberMap = {}

    def change(self, index: int, number: int) -> None:
        self.indexCurrentNumberMap[index] = number
        if number not in self.numberListIndexMap:
            self.numberListIndexMap[number] = []
        heapq.heappush(self.numberListIndexMap[number], index)

    def find(self, number: int) -> int:
        if number not in self.numberListIndexMap:
            return -1
        while self.numberListIndexMap[number]:
            minIndex = self.numberListIndexMap[number][0]
            if self.indexCurrentNumberMap[minIndex] == number:
                return minIndex
            heapq.heappop(self.numberListIndexMap[number])
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)