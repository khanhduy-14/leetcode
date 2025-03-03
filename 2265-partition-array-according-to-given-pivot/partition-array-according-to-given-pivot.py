class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        sn, ln, en =[], [], []
        for i in nums:
            if i == pivot:
                en.append(i)
            elif i > pivot:
                ln.append(i)
            else:
                sn.append(i)
        

        return sn + en + ln