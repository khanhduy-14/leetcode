class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        heap = Heap(nums)
        res = 0
        while heap.heap[1] < k:
            res += 1
            minimum1 = heap.pop()
            minimum2 = heap.pop()
            newNum = min(minimum1, minimum2) * 2 + max(minimum1, minimum2)
            heap.push(newNum)
        return res
        

class Heap:
    def __init__(self, array: List[int]):
        self.heapify(array)
    def push(self, num: int):
        self.heap.append(num)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]

        self.heap[1] = self.heap.pop()

        i = 1
        while i * 2 < len(self.heap):
            if i * 2 + 1 < len(self.heap) and self.heap[i*2+1] < self.heap[i*2] and self.heap[i*2+1] < self.heap[i]:
                self.heap[i], self.heap[i*2 +1] = self.heap[i*2 + 1], self.heap[i]
                i = i * 2 + 1
            elif self.heap[i*2] < self.heap[i]:
                self.heap[i], self.heap[i*2] = self.heap[i*2], self.heap[i]
                i = i * 2
            else:
                break;
        return res
    def heapify(self, array: List[int]) -> List[int]:
        array.append(array[0])
        self.heap = array
        curr = (len(array) - 1) // 2

        while curr > 0:
            i = curr
            while i * 2 < len(self.heap):
                if i * 2 + 1 < len(self.heap) and self.heap[i*2+1] < self.heap[i*2] and self.heap[i*2+1] < self.heap[i]:
                    self.heap[i], self.heap[i*2 +1] = self.heap[i*2 + 1], self.heap[i]
                    i = i * 2 + 1
                elif self.heap[i*2] < self.heap[i]:
                    self.heap[i], self.heap[i*2] = self.heap[i*2], self.heap[i]
                    i = i * 2
                else:
                    break;
            curr-=1
        
