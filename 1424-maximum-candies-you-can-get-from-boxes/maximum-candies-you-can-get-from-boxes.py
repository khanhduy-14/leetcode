from collections import deque
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        de = deque(initialBoxes)
        locked_boxes=set([])
        res = 0
        while de:
            i = de.popleft()
            if status[i] == 1:
                res+= candies[i]
                de.extend(containedBoxes[i])
                for key in keys[i]:
                    status[key] = 1
                    if key in locked_boxes:
                        de.append(key)
                        locked_boxes.remove(key)
            else:
                locked_boxes.add(i)
            
        return res
        